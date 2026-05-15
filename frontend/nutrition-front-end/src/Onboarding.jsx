import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowRight, TrendingDown, Minus, TrendingUp } from 'lucide-react';
import './assets/Auth.css';
import './assets/Onboarding.css';
import LoadingScreen from './LoadingScreen.jsx';
import msuLogo from './assets/msuWhite1.png';

const BASE_URL = import.meta.env.VITE_API_URL;
const CAL_PRESETS = [1800, 2000, 2200, 2500, 2800];

const GOALS = [
  { value: 'Weight Loss',  label: 'Weight loss',  desc: 'Cut to a leaner target',   Icon: TrendingDown },
  { value: 'Maintenance',  label: 'Maintenance',   desc: 'Hold your current weight', Icon: Minus },
  { value: 'Muscle Gain',  label: 'Muscle gain',   desc: 'Build mass on a surplus',  Icon: TrendingUp },
];

function BrandPane() {
  return (
    <div className="ob-brand" aria-hidden="true">
      <div className="brand-dots" />
      <div className="brand-stripe" />
      <div className="brand-glyph">
        <div className="brand-glyph-ring" />
      </div>

      <div className="brand-top">
        <img src={msuLogo} alt="" className="brand-logo" />
        <span className="brand-wordmark">MSUtrition</span>
      </div>

      <div className="brand-center">
        <p className="brand-eyebrow">
          <span className="pulse-dot" />
          Today's fuel · live
        </p>
        <h2 className="brand-headline">
          Train smart.<br />
          Eat <em>Spartan</em>.
        </h2>
        <p className="brand-subhead">
          Track every macro, micro and meal — purpose-built for Michigan State
          athletes, students, and the dining halls they live in.
        </p>
        <div className="brand-stats">
          <div className="stat-card" style={{ '--stat-color': '#22c55e' }}>
            <span className="stat-label">Calories</span>
            <span className="stat-number">1,584</span>
            <span className="stat-unit">/ 2,200</span>
          </div>
          <div className="stat-card" style={{ '--stat-color': '#3b82f6' }}>
            <span className="stat-label">Protein</span>
            <span className="stat-number">84</span>
            <span className="stat-unit">g</span>
          </div>
          <div className="stat-card" style={{ '--stat-color': '#ef4444' }}>
            <span className="stat-label">Carbs</span>
            <span className="stat-number">202</span>
            <span className="stat-unit">g</span>
          </div>
        </div>
      </div>

      <div className="brand-footer">
        <span>v1.0</span>
        <span className="brand-sep">·</span>
        <span>© MSU 2026</span>
        <span className="brand-sep">·</span>
        <span>Go Green</span>
      </div>
    </div>
  );
}

const Onboarding = ({ setIsLoggedIn }) => {
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => { setIsLoading(false); }, []);

  const [formData, setFormData] = useState({
    currentWeight: '',
    goalWeight: '',
    goal: 'Weight Loss',
    goalCalories: '',
    goalProtein: '',
    goalCarbs: '',
    goalFat: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const setGoal = (value) => setFormData(prev => ({ ...prev, goal: value }));

  const setCalPreset = (cal) =>
    setFormData(prev => ({ ...prev, goalCalories: String(cal) }));

  const canSubmit =
    formData.currentWeight !== '' &&
    formData.goalWeight    !== '' &&
    formData.goalCalories  !== '' &&
    formData.goalProtein   !== '' &&
    formData.goalCarbs     !== '' &&
    formData.goalFat       !== '';

  const handleSubmit = async (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (!canSubmit) return;
    await progress(formData);
    setIsLoggedIn(true);
    navigate('/');
  };

  const progress = async (data) => {
    try {
      const response = await fetch(`${BASE_URL}api/update-progress/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const json = await response.json();
        console.log('Success', json);
      }
    } catch (error) {
      console.log('Failed to post', error);
    }
  };

  const goalCal      = Number(formData.goalCalories) || 0;
  const proteinG     = Number(formData.goalProtein)  || 0;
  const carbsG       = Number(formData.goalCarbs)    || 0;
  const fatG         = Number(formData.goalFat)      || 0;
  const proteinKcal  = proteinG * 4;
  const carbsKcal    = carbsG   * 4;
  const fatKcal      = fatG     * 9;
  const totalMacroKcal = proteinKcal + carbsKcal + fatKcal;
  const proteinPct   = goalCal > 0 ? Math.round((proteinKcal / goalCal) * 100) : 0;
  const carbsPct     = goalCal > 0 ? Math.round((carbsKcal   / goalCal) * 100) : 0;
  const fatPct       = goalCal > 0 ? Math.round((fatKcal     / goalCal) * 100) : 0;
  const matchesTarget = goalCal > 0 && Math.abs(totalMacroKcal - goalCal) / goalCal < 0.05;

  const barBase       = totalMacroKcal || 1;
  const proteinBarPct = (proteinKcal / barBase) * 100;
  const carbsBarPct   = (carbsKcal   / barBase) * 100;
  const fatBarPct     = (fatKcal     / barBase) * 100;

  if (isLoading) return <LoadingScreen />;

  return (
    <div className="ob-screen">
      <BrandPane />

      <div className="ob-form-pane">
        <form className="ob-card" onSubmit={handleSubmit} noValidate>

          {/* ── Header ── */}
          <div className="ob-header">
            <p className="ob-eyebrow">Setup your profile</p>
            <h1 className="ob-title">Build your Spartan plate.</h1>
            <p className="ob-subtitle">
              One minute. You can adjust everything later from Settings.
            </p>
          </div>

          {/* ── Primary Goal ── */}
          <div className="ob-section">
            <div className="ob-section-label">
              <span className="ob-section-dot" />
              Primary goal
            </div>
            <div className="ob-goal-grid">
              {GOALS.map(({ value, label, desc, Icon }) => (
                <button
                  key={value}
                  type="button"
                  className={`ob-goal-card${formData.goal === value ? ' ob-goal-card--active' : ''}`}
                  onClick={() => setGoal(value)}
                >
                  <span className="ob-goal-icon"><Icon size={15} /></span>
                  <span className="ob-goal-label">{label}</span>
                  <span className="ob-goal-desc">{desc}</span>
                </button>
              ))}
            </div>
          </div>

          {/* ── Body Composition ── */}
          <div className="ob-section">
            <div className="ob-section-label">
              <span className="ob-section-dot ob-section-dot--blue" />
              Body composition
              <span className="ob-section-unit">lbs</span>
            </div>
            <div className="ob-weight-row">
              <div className="ob-weight-group">
                <label className="ob-field-label">Current weight</label>
                <input
                  className="ob-weight-input"
                  type="number"
                  name="currentWeight"
                  placeholder="175"
                  value={formData.currentWeight}
                  onChange={handleChange}
                />
              </div>
              <span className="ob-arrow" aria-hidden="true">→</span>
              <div className="ob-weight-group">
                <label className="ob-field-label">Goal weight</label>
                <input
                  className="ob-weight-input"
                  type="number"
                  name="goalWeight"
                  placeholder="165"
                  value={formData.goalWeight}
                  onChange={handleChange}
                />
              </div>
            </div>
          </div>

          {/* ── Calorie Target ── */}
          <div className="ob-section">
            <div className="ob-section-label">
              <span className="ob-section-dot ob-section-dot--amber" />
              Calorie target
              <span className="ob-section-unit">kcal / day</span>
            </div>
            <div className="ob-cal-main">
              <span className="ob-field-label">Calories</span>
              <input
                className="ob-cal-input"
                type="number"
                name="goalCalories"
                placeholder="2200"
                value={formData.goalCalories}
                onChange={handleChange}
              />
              <span className="ob-cal-unit">kcal · split below</span>
            </div>
            <div className="ob-cal-presets">
              {CAL_PRESETS.map(preset => (
                <button
                  key={preset}
                  type="button"
                  className={`ob-cal-preset${Number(formData.goalCalories) === preset ? ' ob-cal-preset--active' : ''}`}
                  onClick={() => setCalPreset(preset)}
                >
                  {preset.toLocaleString()}
                </button>
              ))}
            </div>
          </div>

          {/* ── Macro Split ── */}
          <div className="ob-section">
            <div className="ob-section-label">
              <span className="ob-section-dot ob-section-dot--multi" />
              Macro split
              {totalMacroKcal > 0 && (
                <span className="ob-section-unit">
                  {totalMacroKcal.toLocaleString()} of {goalCal.toLocaleString()} kcal
                </span>
              )}
            </div>

            <div className="ob-macro-grid">
              {/* Protein */}
              <div className="ob-macro-card ob-macro-card--protein">
                <span className="ob-macro-label">Protein</span>
                <input
                  className="ob-macro-input"
                  type="number"
                  name="goalProtein"
                  placeholder="0"
                  value={formData.goalProtein}
                  onChange={handleChange}
                />
                <div className="ob-macro-meta">
                  <span className="ob-macro-pct">{proteinPct}%</span>
                  <span className="ob-macro-kcal">{proteinKcal} kcal</span>
                </div>
              </div>

              {/* Carbs */}
              <div className="ob-macro-card ob-macro-card--carbs">
                <span className="ob-macro-label">Carbs</span>
                <input
                  className="ob-macro-input"
                  type="number"
                  name="goalCarbs"
                  placeholder="0"
                  value={formData.goalCarbs}
                  onChange={handleChange}
                />
                <div className="ob-macro-meta">
                  <span className="ob-macro-pct">{carbsPct}%</span>
                  <span className="ob-macro-kcal">{carbsKcal} kcal</span>
                </div>
              </div>

              {/* Fat */}
              <div className="ob-macro-card ob-macro-card--fat">
                <span className="ob-macro-label">Fat</span>
                <input
                  className="ob-macro-input"
                  type="number"
                  name="goalFat"
                  placeholder="0"
                  value={formData.goalFat}
                  onChange={handleChange}
                />
                <div className="ob-macro-meta">
                  <span className="ob-macro-pct">{fatPct}%</span>
                  <span className="ob-macro-kcal">{fatKcal} kcal</span>
                </div>
              </div>
            </div>

            {totalMacroKcal > 0 && (
              <div className="ob-pcf-bar">
                <div className="ob-pcf-seg ob-pcf-seg--protein" style={{ width: `${proteinBarPct}%` }} />
                <div className="ob-pcf-seg ob-pcf-seg--carbs"   style={{ width: `${carbsBarPct}%` }} />
                <div className="ob-pcf-seg ob-pcf-seg--fat"     style={{ width: `${fatBarPct}%` }} />
              </div>
            )}

            <div className="ob-pcf-legend">
              <span className="ob-pcf-label">P · C · F split</span>
              {matchesTarget && (
                <span className="ob-pcf-match">✓ matches target</span>
              )}
            </div>
          </div>

          {/* ── Submit ── */}
          <div className="ob-submit-row">
            <p className="ob-hint">
              {canSubmit ? 'Adjust anytime from Settings' : 'Fill in all fields to continue'}
            </p>
            <button type="submit" className="ob-cta" disabled={!canSubmit}>
              Save &amp; continue
              <ArrowRight size={18} strokeWidth={2.5} className="ob-cta-arrow" />
            </button>
          </div>

        </form>
      </div>
    </div>
  );
};

export default Onboarding;
