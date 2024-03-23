// import { useEffect, useState } from "react";

// const FetchDataComponent = () => {
//   const [message, setMessage] = useState("Loading...");
//   const [people, setPeople] = useState("Loading...");

//   useEffect(() => {
//     // Make sure to use window.fetch or a different name for your fetch function to avoid conflicts with the global fetch
//     window.fetch("http://127.0.0.1:8080/api/home")
//       .then((response) => response.json())
//       .then((data) => {
//         console.log(data);
//         // Assuming 'data.message' contains the message you want to display
//         setMessage(data.message || "Data loaded successfully");
//         setPeople(data.people || "Data loaded successfully");
//       })
//       .catch((error) => {
//         console.error("Error fetching data: ", error);
//         setMessage("Failed to load data");
//       });
//   }, []); // Empty dependency array means this effect runs once on mount

//   return (

//     <div>
    
//     <div>
//       <h1>{message}</h1>
//       <h1>{people}</h1>
    
//     </div>
//     </div>
//   );
// };

// export default FetchDataComponent;



// // {people.map((name)=> (
// //   <div key={name}>
// //     <h1>{name[0]}</h1>

  

// //   </div>


// // ))}