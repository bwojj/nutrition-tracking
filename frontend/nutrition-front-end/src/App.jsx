import Header from "./Header"
import MainBox from "./MainBox"
import { MealsContext } from "./Context/Context"
import { useState } from "react"
import './assets/index.css'

function App() {

  const [meals, setMeals] = useState(["Breakfast", "Lunch", "Dinner", "Snacks"]);
  const [isMicroModalOpen, setIsMicroModalOpen] = useState(false);
  const [isProgressModalOpen, setIsProgressModalOpen] = useState(false);

  return (
    <>
      <MealsContext.Provider value={{ meals, setMeals}}>
          <Header isMicroModalOpen={isMicroModalOpen} setIsMicroModalOpen={setIsMicroModalOpen}
                isProgressModalOpen={isProgressModalOpen} setIsProgressModalOpen={setIsProgressModalOpen}
          />
          <MainBox isMicroModalOpen={isMicroModalOpen} setIsMicroModalOpen={setIsMicroModalOpen}
                isProgressModalOpen={isProgressModalOpen} setIsProgressModalOpen={setIsProgressModalOpen}
          />
      </MealsContext.Provider>
    </>
  )
}

export default App
