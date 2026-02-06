import {useEffect,useState} from "react"

export default function History(){

 const [list,setList]=useState([])
 const [selected,setSelected]=useState(null)
 const [loading,setLoading]=useState(false)
 const [error,setError]=useState(null)

 useEffect(()=>{

   fetch("https://ai-wiki-backend-lfjm.onrender.com/history")
   .then(res=>res.json())
   .then(data=>setList(data))
   .catch(()=>setError("Failed to load history"))

 },[])

 const loadDetails = async(id)=>{

   setLoading(true)

   try{
     const res = await fetch(`https://ai-wiki-backend-lfjm.onrender.com/quiz/${id}`)
     const data = await res.json()
     setSelected(data)
   }catch{
     setError("Failed to load quiz")
   }

   setLoading(false)
 }

 const closeModal = ()=> setSelected(null)

 return(

   <div className="history-container">

     <h2>Past Quizzes</h2>

     {error && <p className="error">{error}</p>}

     {list.length === 0 && <p>No quizzes yet.</p>}

     <table className="history-table">

       <thead>
         <tr>
           <th>ID</th>
           <th>URL</th>
           <th>Action</th>
         </tr>
       </thead>

       <tbody>

         {list.map(item=>(

           <tr key={item.id}>
             <td>{item.id}</td>
             <td className="url-cell">{item.url}</td>
             <td>
               <button className="big-btn" onClick={()=>loadDetails(item.id)}>
                 View
               </button>
             </td>
           </tr>

         ))}

       </tbody>

     </table>

     {loading && <p>Loading quiz...</p>}

     {selected && (

       <div className="modal-overlay">

         <div className="modal">

           <button className="close-btn" onClick={closeModal}>✕</button>

           <h2>{selected.title}</h2>
           <p>{selected.summary}</p>

           {selected.quiz.map((q,i)=>(

             <div className="card" key={i}>

               <h3>{q.question}</h3>

               {q.options.map((opt,index)=>(
                 <p key={index}>• {opt}</p>
               ))}

               <span className="badge">{q.difficulty}</span>

               <p className="answer">
                 Answer: {q.answer}
               </p>

               <p className="explanation">{q.explanation}</p>

             </div>

           ))}

         </div>

       </div>

     )}

   </div>

 )

}