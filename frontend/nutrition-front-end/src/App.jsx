import Header from "./Header"
import MainBox from "./MainBox"
import AuthView from "./AuthView"
import { MealsContext } from "./Context/Context"
import { useState } from "react"
import './assets/index.css'

function App() {

  const [meals, setMeals] = useState(["Breakfast", "Lunch", "Dinner", "Snacks"]);
  const [isMicroModalOpen, setIsMicroModalOpen] = useState(false);
  const [isProgressModalOpen, setIsProgressModalOpen] = useState(false);
  const [token, setToken] = useState(localStorage.getItem('access_token'));

  const handleLogin = (newToken) => {
    localStorage.setItem('access_token', newToken);
    setToken(newToken); 
  }

  return (
    <>
      <MealsContext.Provider value={{ meals, setMeals}}>
        {token ? (
          <>
          <Header isMicroModalOpen={isMicroModalOpen} setIsMicroModalOpen={setIsMicroModalOpen}
                isProgressModalOpen={isProgressModalOpen} setIsProgressModalOpen={setIsProgressModalOpen}
          />
          <MainBox isMicroModalOpen={isMicroModalOpen} setIsMicroModalOpen={setIsMicroModalOpen}
                isProgressModalOpen={isProgressModalOpen} setIsProgressModalOpen={setIsProgressModalOpen}
          />
        </>
        ) : (
          <AuthView onLoginSuccess={handleLogin}/>
        )}
        
      </MealsContext.Provider>
    </>
  )
}

export default App
