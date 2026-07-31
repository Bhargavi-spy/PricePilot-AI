import { FaBell, FaSearch, FaUserCircle } from "react-icons/fa";
import "./Navbar.css";

const Navbar = () => {
  return (
    <header className="navbar">
      <div className="search-box">
        <FaSearch />

        <input
          type="text"
          placeholder="Search products..."
        />
      </div>

      <div className="nav-right">
        <FaBell className="icon" />

        <div className="profile">
          <FaUserCircle />

          <span>Bhargavi</span>
        </div>
      </div>
    </header>
  );
};

export default Navbar;