import './assets/SavedMealForm.css';
import { useState, useEffect } from 'react';
import { useDaysContext } from './Context/DayContext.jsx';
import { addSavedMeal } from './api/mealApi.js';
import { Search, X } from 'lucide-react';

function SavedMealForm({ isOpen, onClose, recentFoods = [], setIsLoading, searchFoodsDB }) {
    const { selectedDate } = useDaysContext();

    const [name, setName] = useState('');
    const [selected, setSelected] = useState(() => new Set());
    const [selectedFoodsMap, setSelectedFoodsMap] = useState(() => new Map());
    const [servings, setServings] = useState({});
    const [formData, setFormData] = useState({
        custom_meal_name: '',
        ids: [],
        date: selectedDate,
    });

    const [searchQuery, setSearchQuery] = useState('');
    const [searchResults, setSearchResults] = useState([]);
    const [lastSearchedQuery, setLastSearchedQuery] = useState('');

    const isSearchMode = !!searchQuery.trim();
    const isSearching = isSearchMode && searchQuery !== lastSearchedQuery;
    const displayFoods = isSearchMode ? searchResults : recentFoods;

    useEffect(() => {
        if (!searchQuery.trim()) return;
        const timer = setTimeout(async () => {
            const results = await searchFoodsDB?.(searchQuery);
            setSearchResults(results || []);
            setLastSearchedQuery(searchQuery);
        }, 300);
        return () => clearTimeout(timer);
    }, [searchQuery, searchFoodsDB]);

    function updateFormData(sel, mealName) {
        setFormData({ custom_meal_name: mealName, ids: [...sel], date: selectedDate });
    }

    function toggle(food) {
        const nextSel = new Set(selected);
        const nextMap = new Map(selectedFoodsMap);
        if (nextSel.has(food.id)) {
            nextSel.delete(food.id);
            nextMap.delete(food.id);
        } else {
            nextSel.add(food.id);
            nextMap.set(food.id, food);
        }
        setSelected(nextSel);
        setSelectedFoodsMap(nextMap);
        updateFormData(nextSel, name);
    }

    function handleServingChange(foodId, val) {
        setServings(prev => ({ ...prev, [foodId]: val }));
    }

    function getScale(food) {
        const m = food.serving_size?.match(/^([\d.]+)/);
        const origNum = parseFloat(m?.[1]) || 1;
        const raw = servings[food.id];
        const current = raw !== undefined ? (parseFloat(raw) || 0) : origNum;
        return origNum > 0 ? current / origNum : 1;
    }

    const totals = (() => {
        let cal = 0, p = 0, c = 0, f = 0;
        selectedFoodsMap.forEach(food => {
            const scale = getScale(food);
            cal += food.calories * scale;
            p += food.protein * scale;
            c += food.carbs * scale;
            f += food.fat * scale;
        });
        return { cal: Math.round(cal), p: Math.round(p), c: Math.round(c), f: Math.round(f) };
    })();

    const canSubmit = name.trim().length > 0 && selected.size > 0;

    if (!isOpen) return null;

    const n = selected.size;

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!canSubmit) return;
        setIsLoading(true);
        await addSavedMeal(formData.custom_meal_name, formData.ids);
        setIsLoading(false);
        onClose();
    };

    return (
        <div className="sm-overlay">
            <div
                className="sm-card"
                role="dialog"
                aria-labelledby="sm-title"
            >
                {/* HEADER */}
                <div className="sm-header">
                    <div className="sm-header-text">
                        <div className="sm-eyebrow">Add to library</div>
                        <h2 className="sm-title" id="sm-title">Create Saved Meal</h2>
                        <div className="sm-subtitle">Name it, then pick foods from your recents</div>
                    </div>
                    <button type="button" className="sm-close" aria-label="Close" onClick={onClose}>✕</button>
                </div>

                {/* BODY — meal name */}
                <div className="sm-body">
                    <label className="sm-field">
                        <span className="sm-field-label">Meal name</span>
                        <input
                            type="text"
                            placeholder="e.g. Post-workout shake"
                            value={name}
                            onChange={(e) => {
                                setName(e.target.value);
                                updateFormData(selected, e.target.value);
                            }}
                            autoComplete="off"
                        />
                    </label>
                </div>

                {/* SEARCH */}
                <div className="sm-search-row">
                    <div className="sm-search-wrap">
                        <Search className="sm-search-icon" size={15} />
                        <input
                            className="sm-search-input"
                            type="text"
                            placeholder="Search all foods…"
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            autoComplete="off"
                        />
                        {searchQuery && (
                            <button className="sm-search-clear" onClick={() => setSearchQuery('')} aria-label="Clear search">
                                <X size={14} />
                            </button>
                        )}
                    </div>
                </div>

                {/* SECTION HEADER */}
                <div className="sm-section">
                    <span className="sm-section-title">
                        {isSearchMode ? (
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
                                <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
                            </svg>
                        ) : (
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
                                <circle cx="12" cy="12" r="9" />
                                <polyline points="12 7 12 12 15 14" />
                            </svg>
                        )}
                        {isSearchMode ? 'Results' : 'Recents'}
                    </span>
                    <span className={`sm-section-count${n > 0 ? ' has-selection' : ''}`}>
                        {n} selected
                    </span>
                </div>

                {/* SCROLLABLE LIST */}
                <div className="sm-list">
                    {isSearching ? (
                        <div className="sm-searching">Searching…</div>
                    ) : displayFoods.length === 0 ? (
                        <div className="sm-empty">
                            {isSearchMode ? 'No foods found.' : 'No recent foods yet — log something first.'}
                        </div>
                    ) : (
                        displayFoods.map((food) => {
                            const isSel = selected.has(food.id);
                            const servMatch = food.serving_size?.match(/^([\d.]+)\s*(.*)/);
                            const servNum = servMatch ? servMatch[1] : '1';
                            const servUnit = servMatch ? (servMatch[2] || 'g') : 'g';
                            const scale = getScale(food);
                            return (
                                <div
                                    key={food.id}
                                    className={`sm-row${isSel ? ' is-selected' : ''}`}
                                    role="checkbox"
                                    aria-checked={isSel}
                                    tabIndex={0}
                                    onClick={() => toggle(food)}
                                    onKeyDown={(e) => {
                                        if (e.key === ' ' || e.key === 'Enter') {
                                            e.preventDefault();
                                            toggle(food);
                                        }
                                    }}
                                >
                                    <div className="sm-check">
                                        <svg viewBox="0 0 24 24">
                                            <polyline points="5 12 10 17 19 7" />
                                        </svg>
                                    </div>
                                    <div className="sm-row-text">
                                        <div className="sm-row-name">{food.food_name}</div>
                                        <div className="sm-row-meta">
                                            {food.brand && (<><span>{food.brand}</span><span className="dot">·</span></>)}
                                            <span>{food.serving_size}</span>
                                        </div>
                                        {isSel && (
                                            <div className="sm-inline-macros">
                                                <span><span className="mp">P</span> {Math.round(food.protein * scale)}</span>
                                                <span><span className="mc">C</span> {Math.round(food.carbs * scale)}</span>
                                                <span><span className="mf">F</span> {Math.round(food.fat * scale)}</span>
                                                <span className="cal">{Math.round(food.calories * scale)} cal</span>
                                            </div>
                                        )}
                                    </div>
                                    <div className="sm-row-macros">
                                        <span><span className="mp">P</span> {Math.round(food.protein * scale)}</span>
                                        <span><span className="mc">C</span> {Math.round(food.carbs * scale)}</span>
                                        <span><span className="mf">F</span> {Math.round(food.fat * scale)}</span>
                                        <span className="cal">{Math.round(food.calories * scale)} cal</span>
                                    </div>
                                    <div className="sm-row-serving" onClick={(e) => e.stopPropagation()}>
                                        <span className="sm-serving-label">Serving</span>
                                        <div className="sm-serving-input-wrap">
                                            <input
                                                type="number"
                                                className="sm-serving-input"
                                                value={servings[food.id] !== undefined ? servings[food.id] : servNum}
                                                onChange={(e) => handleServingChange(food.id, e.target.value)}
                                            />
                                            <span className="sm-serving-unit">{servUnit}</span>
                                        </div>
                                    </div>
                                </div>
                            );
                        })
                    )}
                </div>

                {/* FOOTER */}
                <div className="sm-footer">
                    <div className="sm-summary">
                        <span><span className="label">Total </span><span className="sm-summary-cal">{totals.cal}</span> cal</span>
                        <span><span style={{ color: 'var(--macro-protein)' }}>P</span> {totals.p}</span>
                        <span><span style={{ color: 'var(--macro-carbs)' }}>C</span> {totals.c}</span>
                        <span><span style={{ color: 'var(--macro-fat)' }}>F</span> {totals.f}</span>
                    </div>
                    <button
                        type="button"
                        className="sm-btn sm-btn-primary"
                        disabled={!canSubmit}
                        onClick={handleSubmit}
                    >
                        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                            <path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z" />
                            <polyline points="17 21 17 13 7 13 7 21" />
                            <polyline points="7 3 7 8 15 8" />
                        </svg>
                        Add to Saved Meals
                    </button>
                </div>
            </div>
        </div>
    );
}

export default SavedMealForm;
