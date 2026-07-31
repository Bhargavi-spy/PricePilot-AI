import {
  FaTachometerAlt,
  FaBoxOpen,
  FaShoppingCart,
  FaChartLine,
  FaRobot,
  FaWarehouse,
  FaUserCircle,
  FaCog,
} from "react-icons/fa";
import { NavLink } from "react-router-dom";

import "./Navbar.css";
import "./Sidebar.css";

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <div className="logo">
        <h2>🚀 PricePilot AI</h2>
      </div>

      <nav className="menu">
        <NavLink to="/" className={({ isActive }) => (isActive ? "active" : "")}
        >
          <FaTachometerAlt />
          <span>Dashboard</span>
        </NavLink>

        <NavLink to="/products" className={({ isActive }) => (isActive ? "active" : "")}
        >
          <FaBoxOpen />
          <span>Products</span>
        </NavLink>

        <NavLink to="/sales" className={({ isActive }) => (isActive ? "active" : "")}
        >
          <FaShoppingCart />
          <span>Sales</span>
        </NavLink>

        <NavLink to="/analytics" className={({ isActive }) => (isActive ? "active" : "")}
        >
          <FaChartLine />
          <span>Analytics</span>
        </NavLink>

        <NavLink to="/pricing" className={({ isActive }) => (isActive ? "active" : "")}
        >
          <FaRobot />
          <span>AI Pricing</span>
        </NavLink>

        <NavLink to="/inventory" className={({ isActive }) => (isActive ? "active" : "")}
        >
          <FaWarehouse />
          <span>Inventory</span>
        </NavLink>

        <NavLink to="/profile" className={({ isActive }) => (isActive ? "active" : "")}
        >
          <FaUserCircle />
          <span>Profile</span>
        </NavLink>

        <NavLink to="/settings" className={({ isActive }) => (isActive ? "active" : "")}
        >
          <FaCog />
          <span>Settings</span>
        </NavLink>
      </nav>
    </aside>
  );
};

export default Sidebar;