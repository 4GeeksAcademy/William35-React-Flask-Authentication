import React from "react";
import { Link,useNavigate } from "react-router-dom";

export const Navbar = () => {
	let navigate = useNavigate()
	function logout(){
		sessionStorage.removeItem("token")
		navigate("/")
	}
	return (
		<nav className="navbar navbar-light bg-light">
			<Link to="/login"><button>
				login
			</button></Link>
			<Link to="/signup"><button>
				signup
			</button></Link>
			<Link to="/private"><button>
				private
			</button></Link>
			<button onClick={()=> logout()}>logout</button>
		</nav>
	);
};
