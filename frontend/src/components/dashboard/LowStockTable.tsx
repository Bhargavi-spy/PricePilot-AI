const LowStockTable = () => {
  return (
    <div className="panel">

      <h2>Low Stock Products</h2>

      <table>

        <thead>
          <tr>
            <th>Product</th>
            <th>Stock</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Mouse</td>
            <td>4</td>
          </tr>

          <tr>
            <td>Monitor</td>
            <td>3</td>
          </tr>

        </tbody>

      </table>

    </div>
  );
};

export default LowStockTable;