import { Outlet } from "react-router-dom";
import Sidebar from "../Sidebar";
import Topbar from "./Topbar";
import Footer from "./Footer";
import "./MainLayout.css";

const MainLayout = () => {
  return (
    <div className="app-shell">
      <Sidebar />
      <div className="app-view">
        <Topbar />
        <main className="app-content">
          <Outlet />
        </main>
        <Footer />
      </div>
    </div>
  );
};

export default MainLayout;