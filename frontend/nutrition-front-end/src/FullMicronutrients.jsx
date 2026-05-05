import { createPortal } from "react-dom";
import './assets/RefinedModal.css'
import './assets/FullMicronutrients.css'

function FullMicronutrients({ isOpen, onClose, foodData }){

    let microTotals = {
        fiber: 0,
        sugar: 0,
        saturated_fat: 0,
        polyunsaturated_fat: 0,
        monounsaturated_fat: 0,
        trans_fat: 0,
        cholesterol: 0,
        sodium: 0,
        potassium: 0,
        vitamin_A: 0,
        vitamin_C: 0,
        calcium: 0,
    }
    foodData.forEach(food => {
       Object.keys(microTotals).forEach(key => {
            microTotals[key] += food[key];
       })
    })

    if (!isOpen) return null;
    console.log(microTotals)
    return createPortal(
        <div className="refined-overlay" onClick={onClose}>
            <div className="refined-modal" onClick={(e) => e.stopPropagation()}>

                <div className="refined-modal-header">
                    <div>
                        <div className="refined-eyebrow">Today</div>
                        <h2 className="refined-title">Micronutrients</h2>
                    </div>
                    <button className="refined-close" onClick={onClose}>✕</button>
                </div>

                <div className="micro-body">
                    <MicroSection title="Vitamins" items={[
                        { label: 'Vitamin A', amount: microTotals.vitamin_A, goal: 900,  unit: 'mcg', tone: 'blue' },
                        { label: 'Vitamin C', amount: microTotals.vitamin_C, goal: 90,   unit: 'mg',  tone: 'orange' },
                        { label: 'Fiber',     amount: microTotals.fiber,     goal: 23,   unit: 'g',   tone: 'purple' },
                        { label: 'Sugar',     amount: microTotals.sugar,     goal: 41,   unit: 'g',   tone: 'orange' },
                    ]}/>
                    <MicroSection title="Minerals" items={[
                        { label: 'Sodium',      amount: microTotals.sodium,      goal: 2300, unit: 'mg', tone: 'purple' },
                        { label: 'Potassium',   amount: microTotals.potassium,   goal: 4700, unit: 'mg', tone: 'blue' },
                        { label: 'Calcium',     amount: microTotals.calcium,     goal: 1300, unit: 'mg', tone: 'blue' },
                        { label: 'Cholesterol', amount: microTotals.cholesterol, goal: 300,  unit: 'mg', tone: 'orange' },
                    ]}/>
                    <MicroSection title="Fats" items={[
                        { label: 'Saturated Fat',     amount: microTotals.saturated_fat,     goal: 16, unit: 'g', tone: 'orange' },
                        { label: 'Monounsaturated Fat', amount: microTotals.monounsaturated_fat, goal: 0, unit: 'g', tone: 'blue' },
                        { label: 'Polyunsaturated Fat', amount: microTotals.polyunsaturated_fat, goal: 0, unit: 'g', tone: 'blue' },
                        { label: 'Trans Fat',         amount: microTotals.trans_fat,         goal: 0,  unit: 'g', tone: 'purple' },
                    ]}/>
                </div>

            </div>
        </div>,
        document.body
    );
}

function MicroSection({ title, items }) {
    return (
        <section>
            <div className="micro-section-header">
                <span className="micro-section-title">{title}</span>
                <span className="micro-section-meta">Today / Goal</span>
            </div>
            <div className="micro-section-rows">
                {items.map(m => <MicroRow key={m.label} {...m}/>)}
            </div>
        </section>
    );
}

function MicroRow({ label, amount, goal, unit, tone }) {
    const pct = goal > 0 ? Math.min(100, Math.round((amount / goal) * 100)) : 0;
    return (
        <div className="micro-row">
            <div className={`micro-tone-square micro-tone-square--${tone}`}>
                {label.slice(0, 2).toUpperCase()}
            </div>
            <div className="micro-center">
                <div className="micro-center-top">
                    <span className="micro-name">{label}</span>
                    <span className="micro-pct">{pct}%</span>
                </div>
                <div className="micro-progress-track">
                    <div
                        className={`micro-progress-fill micro-progress-fill--${tone}`}
                        style={{ width: `${pct}%` }}
                    />
                </div>
            </div>
            <div className="micro-numeric">
                <span className="micro-numeric-amount">{amount}</span>
                <span className="micro-numeric-goal"> / {goal}</span>
                <span className="micro-numeric-unit">{unit}</span>
            </div>
        </div>
    );
}

export default FullMicronutrients
