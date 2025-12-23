import Header from "./Header"
import MainBox from "./MainBox"
import { MealsContext } from "./Context/Context"
import { useState } from "react"
import './assets/index.css'

function App() {

  const [meals, setMeals] = useState(["Breakfast", "Lunch", "Dinner", "Snacks"]);

  return (
    <>
      <MealsContext.Provider value={{ meals, setMeals}}>
        <Header/>
        <MainBox/>
      </MealsContext.Provider>
    </>
  )
}

export default App
