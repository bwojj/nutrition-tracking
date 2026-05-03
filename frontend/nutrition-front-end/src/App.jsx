import './assets/index.css'
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom"
import { MealsContext } from "./Context/Context.js"
import { DaysProvider } from './Context/DayContext.jsx'
import { useState, useEffect } from "react"
import Header from "./Header.jsx"
import MainBox from "./MainBox.jsx"
import Onboarding from "./Onboarding.jsx"
import Auth from "./Auth.jsx"
import LoadingScreen from "./LoadingScreen.jsx"
import { is_authenticated } from "./api.js"
import { getUserData } from "./api/userApi.js"

function App() {

  const [meals, setMeals] = useState(["Breakfast", "Lunch", "Dinner", "Snacks"]);
  const [isMicroModalOpen, setIsMicroModalOpen] = useState(false);
  const [isProgressModalOpen, setIsProgressModalOpen] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState("");

  const [isLoading, setIsLoading] = useState(true);


useEffect(() => {
  const initializeApp = async () => {
    setIsLoading(true);
    try {
      const authData = await is_authenticated();
      
      if (authData?.authenticated) {
        setIsLoggedIn(true);
        const user = await getUserData();
        if (user) setUsername(user);
      }
    } catch (error) {
      console.error("Initialization error", error);
    } finally{
      setIsLoading(false);
    }
  };

  initializeApp();
}, []);

if(isLoading){
  return <LoadingScreen/>
}
  return (
    <Router>
      <DaysProvider>
      <MealsContext.Provider value={{ meals, setMeals}}>
        <Routes>
          <Route
            path="/login"
            element= {<Auth setIsLoggedIn={setIsLoggedIn} setIsLoading={setIsLoading}/>}
          />
          <Route
            path="/"
            element={isLoggedIn ? 
              <>
              <Header isMicroModalOpen={isMicroModalOpen} setIsMicroModalOpen={setIsMicroModalOpen}
                  isProgressModalOpen={isProgressModalOpen} setIsProgressModalOpen={setIsProgressModalOpen}
                  setIsLoggedIn={setIsLoggedIn} username={username}
              />
              <MainBox 
                isLoggedIn={isLoggedIn} 
                isMicroModalOpen={isMicroModalOpen} 
                setIsMicroModalOpen={setIsMicroModalOpen}
                isProgressModalOpen={isProgressModalOpen} 
                setIsProgressModalOpen={setIsProgressModalOpen} 
                setIsLoading={setIsLoading}
                isLoading={isLoading}
              /></> : <Navigate to="/login"/>}
          />
          <Route
            path="/onboarding"
            element={
              <Onboarding 
              setIsLoggedIn={setIsLoggedIn}
              />
            }
          />
        </Routes>
          
      </MealsContext.Provider>
      </DaysProvider>
      
    </Router>
  );
}

export default App
