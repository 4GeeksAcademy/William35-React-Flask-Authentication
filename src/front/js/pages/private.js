import React, { useContext, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Context } from "../store/appContext";

function Private(){
    const { store, actions } = useContext(Context);
  const navigate = useNavigate()
  useEffect(()=>{
    if(!sessionStorage.getItem("token")){
        navigate("/login")
    }
  },[])
    return <h1>Hello World</h1>
}
export default Private