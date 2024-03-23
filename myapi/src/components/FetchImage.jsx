import { useEffect, useState } from "react";

const FetchImage = () => {
    const [img_fetch, setImg_Fetch] = useState("Loading...");
   
  
    useEffect(() => {
      // Make sure to use window.fetch or a different name for your fetch function to avoid conflicts with the global fetch
      window.fetch("http://127.0.0.1:8080/imagegen")
        .then((response) => response.json())
        .then((data1) => {
          console.log(data1);
          // Assuming 'data.message' contains the message you want to display
          setImg_Fetch(data1.img_fetch) || "Data loaded successfully"
       
        })
        .catch((error) => {
          console.error("Error fetching data: ", error);
          setImg_Fetch("Failed to load data");
        });
    }, [])
 
  return (
    <div>
        <h1>IMAGE CREATION</h1>
        {img_fetch}
      
    </div>
  )
}

export default FetchImage 
