const NotFound = () => {
  return (
    <div className="panel">
      <div className="section-title">
        <div>
          <h2>Page not found</h2>
          <p>The requested page does not exist.</p>
        </div>
      </div>
      <div className="empty-state">Select a section from the sidebar to continue.</div>
    </div>
  );
};

export default NotFound;
