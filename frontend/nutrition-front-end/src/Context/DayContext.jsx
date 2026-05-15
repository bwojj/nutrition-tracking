import { useState, createContext, useContext } from "react";

const getLocalDateString = () => {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
};

const DaysContext = createContext(); 

export const DaysProvider = ({ children }) => {
    const [selectedDate, setSelectedDate] = useState(getLocalDateString); 

    return (
        <DaysContext.Provider value={{ selectedDate, setSelectedDate }}>
            {children}
        </DaysContext.Provider>
    );
};

// eslint-disable-next-line react-refresh/only-export-components
export const useDaysContext = () => useContext(DaysContext); 