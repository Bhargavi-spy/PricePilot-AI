import axios from "axios";
import { useEffect, useState } from "react";
import {
  FaBoxOpen,
  FaUserFriends,
  FaBell,
  FaChartLine,
  FaLightbulb,
  FaBolt,
} from "react-icons/fa";
import { getDashboard, getLowStockProducts } from "../services/dashboardservice";
import type { DashboardResponse } from "../types/dashboard";
import type { LowStockProduct } from "../types/product";
import "../components/dashboard/Dashboard.css";

const Dashboard = () => {
  const [dashboardData, setDashboardData] = useState<DashboardResponse | null>(null);
  const [lowStock, setLowStock] = useState<LowStockProduct[]>([]);
  const [loading, setLoading] = useState(true);
  const [dashboardError, setDashboardError] = useState("");
  const [lowStockError, setLowStockError] = useState("");

  const getErrorMessage = (err: unknown) => {
    if (axios.isAxiosError(err)) {
      return err.response?.data?.detail ?? err.message;
    }
    return err instanceof Error ? err.message : String(err);
  };

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);

      const [dashboardResult, lowStockResult] = await Promise.allSettled([
        getDashboard(),
        getLowStockProducts(),
      ]);

      if (dashboardResult.status === "fulfilled") {
        setDashboardData(dashboardResult.value);
      } else {
        console.error("Dashboard load failed", dashboardResult.reason);
        setDashboardError(`Unable to load dashboard data: ${getErrorMessage(dashboardResult.reason)}`);
      }

      if (lowStockResult.status === "fulfilled") {
        setLowStock(lowStockResult.value);
      } else {
        console.error("Low stock load failed", lowStockResult.reason);
        setLowStockError(`Unable to load low stock alerts: ${getErrorMessage(lowStockResult.reason)}`);
      }

      setLoading(false);
    };

    loadData();
  }, []);

  const kpis = [
    {
      title: "Total Products",
      value: dashboardData?.total_products?.toLocaleString() ?? "--",
      icon: <FaBoxOpen />,
    },
    {
      title: "Competitors",
      value: "24",
      icon: <FaUserFriends />,
    },
    {
      title: "Active Alerts",
      value: "3",
      icon: <FaBell />,
    },
    {
      title: "Price Changes Today",
      value: "18",
      icon: <FaBolt />,
    },
    {
      title: "Revenue Impact",
      value: dashboardData ? `₹${dashboardData.potential_revenue.toLocaleString()}` : "--",
      icon: <FaChartLine />,
    },
    {
      title: "AI Suggestions",
      value: "12",
      icon: <FaLightbulb />,
    },
  ];

  const activity = [
    { title: "Laptop price updated", meta: "2 mins ago" },
    { title: "AI recommended new margin", meta: "12 mins ago" },
    { title: "Competitor price changed", meta: "35 mins ago" },
    { title: "Alert: low stock item", meta: "1 hr ago" },
  ];

  const connectionStatus = loading
    ? "Loading"
    : dashboardError
    ? "Disconnected"
    : lowStockError
    ? "Partial"
    : "Connected";

  const alertMessage = dashboardError || lowStockError;

  return (
    <div className="dashboard-page">
      <div className="dashboard-header">
        <div>
          <p className="eyebrow">Executive Dashboard</p>
          <h1>PricePilot business intelligence</h1>
          <p className="dashboard-subtitle">
            Monitor pricing performance, competitor dynamics, and AI-driven opportunities in one place.
          </p>
        </div>
        <div className="dashboard-status-box">
          <span>Status</span>
          <strong>{connectionStatus}</strong>
        </div>
      </div>

      {alertMessage && (
        <div className="dashboard-alert">
          <strong>Connection issue</strong>
          <span>{alertMessage}</span>
        </div>
      )}

      <section className="kpi-grid">
        {kpis.map((kpi) => (
          <article key={kpi.title} className="kpi-card">
            <div className="kpi-icon">{kpi.icon}</div>
            <div>
              <p>{kpi.title}</p>
              <h2>{kpi.value}</h2>
            </div>
          </article>
        ))}
      </section>

      <section className="analytics-grid">
        <div className="analytics-panel large">
          <div className="panel-title-row">
            <div>
              <h2>Price Trend</h2>
              <p>Daily movement across priority SKUs.</p>
            </div>
            <span className="badge">Live</span>
          </div>
          <div className="chart-placeholder">📈 Price Trend Chart</div>
        </div>

        <div className="analytics-panel small">
          <h3>Competitor comparison</h3>
          <div className="metric-stack">
            <span>Latest market pricing across top competitors.</span>
          </div>
        </div>

        <div className="analytics-panel small">
          <h3>Revenue trend</h3>
          <div className="metric-stack">
            <span>Estimated revenue performance over the past week.</span>
          </div>
        </div>

        <div className="analytics-panel small">
          <h3>Product performance</h3>
          <div className="metric-stack">
            <span>Top movers and SKU health indicators.</span>
          </div>
        </div>

        <div className="analytics-panel small">
          <h3>Market share</h3>
          <div className="metric-stack">
            <span>Share of active categories versus competition.</span>
          </div>
        </div>

        <div className="analytics-panel small">
          <h3>Category distribution</h3>
          <div className="metric-stack">
            <span>Revenue and stock split by category.</span>
          </div>
        </div>
      </section>

      <section className="bottom-grid">
        <div className="activity-panel">
          <div className="panel-title-row">
            <div>
              <h2>Recent Activity</h2>
              <p>Latest updates, AI decisions, notifications, and alerts.</p>
            </div>
            <span className="badge outline">View all</span>
          </div>

          <div className="activity-group">
            <h3>Latest price updates</h3>
            <ul>
              {activity.map((item) => (
                <li key={item.title}>
                  <strong>{item.title}</strong>
                  <span>{item.meta}</span>
                </li>
              ))}
              {lowStock.length > 0 && (
                <li>
                  <strong>{lowStock[0].name} low stock alert</strong>
                  <span>{lowStock[0].stock} units remaining</span>
                </li>
              )}
            </ul>
          </div>

          <div className="activity-panes">
            <div className="activity-card">
              <h4>Recent AI decisions</h4>
              <p>12 pricing opportunities generated in the last 24 hours.</p>
            </div>
            <div className="activity-card">
              <h4>Notifications</h4>
              <p>4 new competitor price alerts requiring review.</p>
            </div>
            <div className="activity-card">
              <h4>Alerts</h4>
              <p>2 low-stock and 1 pricing gap alert active.</p>
            </div>
          </div>
        </div>

        <aside className="quick-actions-panel">
          <div className="panel-title-row">
            <div>
              <h2>Quick Actions</h2>
              <p>Take action on key pricing workflows.</p>
            </div>
          </div>
          <div className="actions-grid">
            <button>Add Product</button>
            <button>Analyze Prices</button>
            <button>Generate Report</button>
            <button>View Competitors</button>
          </div>
        </aside>
      </section>
    </div>
  );
};

export default Dashboard;
