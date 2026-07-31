import { FaBell, FaSearch, FaMoon, FaUserCircle } from "react-icons/fa";

const Topbar = () => {
  return (
    <div className="topbar">
      <div className="topbar-left">
        <div className="brand">
          <div className="brand-mark">PP</div>
          <div>
            <strong>PricePilot AI</strong>
            <span>Dynamic pricing intelligence</span>
          </div>
        </div>
      </div>

      <div className="topbar-center">
        <div className="search-field">
          <FaSearch />
          <input type="search" placeholder="Search products, competitors, reports..." />
        </div>
      </div>

      <div className="topbar-right">
        <button className="icon-button" aria-label="Notifications">
          <FaBell />
        </button>
        <button className="icon-button" aria-label="Toggle theme">
          <FaMoon />
        </button>
        <button className="profile-button">
          <FaUserCircle />
          <span>Bhargavi</span>
        </button>
      </div>
    </div>
  );
};

export default Topbar;
