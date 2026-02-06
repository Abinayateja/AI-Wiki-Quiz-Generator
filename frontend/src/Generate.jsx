import {useState} from "react"

export default function Generate(){

 const [url,setUrl]=useState("")
 const [data,setData]=useState(null)
 const [loading,setLoading]=useState(false)
 const [message,setMessage]=useState("")

 const generateQuiz = async()=>{
  setLoading(true)

  const res = await fetch("http://127.0.0.1:8000/generate-quiz",{
    method:"POST",
    headers:{ "Content-Type":"application/json" },
    body:JSON.stringify({ url })
  })

  const result = await res.json()

  if(!res.ok){
     alert(result.detail || "Error generating quiz")
     setLoading(false)
     return
  }

  setData(result)
  setLoading(false)
}

 return(

   <div>

     <input
       className="input"
       placeholder="Paste Wikipedia URL"
       value={url}
       onChange={(e)=>setUrl(e.target.value)}
     />

     <button className="big-btn" onClick={generateQuiz}>
       Generate Quiz
     </button>

     {loading && (
  <div className="loader"></div>
)}

     {message && (
       <div className="info-banner">
         {message}
       </div>
     )}

     {data && (

       <div>

         <h2>{data.title}</h2>
         <p>{data.summary}</p>
         {data.related_topics && data.related_topics.length > 0 && (
  <div className="card">
    <h3>Related Topics</h3>

    <div className="topics-container">
      {data.related_topics.map((topic,index)=>(
        <span key={index} className="topic-badge">
          {topic}
        </span>
      ))}
    </div>

  </div>
)}
         {data?.quiz?.map((q,i)=>(

           <div className="card" key={i}>

             <h3>{q.question}</h3>

             {q.options.map((opt,index)=>(
               <p key={index}>• {opt}</p>
             ))}

             <p className={`badge ${q.difficulty}`}>
  {q.difficulty}
</p>
             <p>{q.explanation}</p>

           </div>

         ))}

       </div>

     )}

   </div>
 )
}