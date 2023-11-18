import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-light">
			<Link to="/login"><button>
				login
			</button></Link>
			<Link to="/signup"><button>
				signup
			</button></Link>
		</nav>
	);
};
