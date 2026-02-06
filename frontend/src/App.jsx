import {useState} from "react"
import Generate from "./Generate"
import History from "./History"
import "./index.css"

export default function App(){

  const [tab,setTab]=useState("generate")

  return(

    <div className="container">

      <h1>AI Wiki Quiz Generator</h1>

      <div className="tab-buttons">
        <button onClick={()=>setTab("generate")}>Generate Quiz</button>
        <button onClick={()=>setTab("history")}>Past Quizzes</button>
      </div>

      {tab==="generate" && <Generate/>}
      {tab==="history" && <History/>}

    </div>
  )
}