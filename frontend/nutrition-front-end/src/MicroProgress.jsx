import './assets/MicroProgress.css'

function MicroProgress(props){
    const current = Math.round(((Number(props.current) / Number(props.goal)) * 100)) || 0;
    console.log(current);

    return(
        <div className="micro-progress">
            <div className="micro-progress-fill" style={{width: `${current}%`}}>
            </div>
        </div>
    );
}

export default MicroProgress 