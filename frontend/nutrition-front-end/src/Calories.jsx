import './assets/Calories.css'

function Calories() {
  const r = 190;
  const cx = 200;
  const cy = 210;

  const x1 = cx - r;
  const x2 = cx + r;
  const y  = cy;

  return (
    <div className="calories">
      <h1 className="calorie-title">Total Calories</h1>

      <svg width="500" height="325" viewBox="0 0 400 300">
        <path
          d={`M ${x1} ${y} A ${r} ${r} 0 0 1 ${x2} ${y}`}
          fill="none"
          stroke="green"
          strokeWidth="30"
          strokeLinecap="round"
        />
      </svg>
      <div className="calorie-number-ratio">
        <span className="calorie-number">0</span>
        <span className="calorie-ratio">0 / 3000</span>
      </div>
    </div>
  );
}

export default Calories 