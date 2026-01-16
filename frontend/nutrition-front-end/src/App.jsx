import Header from "./Header"
import MainBox from "./MainBox"
import Onboarding from "./Onboarding"
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom"
import { MealsContext } from "./Context/Context"
import { useState, useEffect } from "react"
import './assets/index.css'
import Auth from "./Auth"
import { is_authenticated } from "./api"
import LoadingScreen from "./LoadingScreen"

function App() {

  const [meals, setMeals] = useState(["Breakfast", "Lunch", "Dinner", "Snacks"]);
  const [isMicroModalOpen, setIsMicroModalOpen] = useState(false);
  const [isProgressModalOpen, setIsProgressModalOpen] = useState(false);
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState("");

  const [isLoading, setIsLoading] = useState(true);

 useEffect(() => {
      const checkAuth = async () => {
        try{
          const data = await is_authenticated();
          
          if (data && data.authenticated) {
            setIsLoggedIn(true);
          } else {
            setIsLoggedIn(false);
          }
        } catch(error){
            console.log("Error Fetch", error);
        } finally {
          setIsLoading(false);
        };
      };

    checkAuth();
  }, []); 

  useEffect(() => {
    localStorage.setItem("isLoggedIn", isLoggedIn);
    getUserData();
  }, [isLoggedIn])

  const getUserData = async () => {
    try{
      const response = await fetch('http://localhost:8000/api/user/', {
        credentials: 'include', 
      })
      if(response.ok){
        const data = await response.json();
        setUsername(data[0].username);
      }
    } catch(error){
      console.log("Failed to fetch", error)
    }
  }

  console.log(username);
  if(isLoading){
    return <LoadingScreen/>;
  }
  return (
    <Router>
      <MealsContext.Provider value={{ meals, setMeals}}>
        <Routes>
          <Route
            path="/login"
            element={!isLoggedIn ? <Auth setIsLoggedIn={setIsLoggedIn}/> : <Navigate to="/"/>}
          />
          <Route
            path="/"
            element={isLoggedIn ? 
              <>
              <Header isMicroModalOpen={isMicroModalOpen} setIsMicroModalOpen={setIsMicroModalOpen}
                  isProgressModalOpen={isProgressModalOpen} setIsProgressModalOpen={setIsProgressModalOpen}
                  setIsLoggedIn={setIsLoggedIn}
              />
              <MainBox isLoggedIn={isLoggedIn} isMicroModalOpen={isMicroModalOpen} setIsMicroModalOpen={setIsMicroModalOpen}
                isProgressModalOpen={isProgressModalOpen} setIsProgressModalOpen={setIsProgressModalOpen}
              /></> : <Navigate to="/login"/>}
          />
          <Route
            path="/onboarding"
            element={<Onboarding/>}
          />
        </Routes>
          
      </MealsContext.Provider>
      
    </Router>
  );
}

export default App
