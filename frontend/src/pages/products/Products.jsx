import { useEffect, useState } from "react";
import api from "../../api/axios";
import styles from "./Products.module.css";

const Products = () => {
  const [productsData, setProductsData] = useState([]);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await api.get("/products");
        setProductsData(response.data);
      } catch (err) {
        console.error(err);
        setError(err.response?.data?.message || err.message || "Failed to fetch products data.");
      } finally {
        setIsLoading(false);
      }
    };

    fetchProducts();
  }, []);

  if (isLoading) return <div className={styles.loading}>Loading products...</div>;
  if (error) return <div className={styles.error}>Error: {error}</div>;

  return (
    <div className={styles.content}>
      <h1 className={styles.title}>Products</h1>
      <ul className={styles.productsList}>
        {productsData.map((product) => (
          <li key={product.id} className={styles.productItem}>
            <h2>{product.name}</h2>
            <p>Type: {product.product_type}</p>
            <p>Quantity: {product.quantity}</p>
            <p>Price: ${product.price.toFixed(2)}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Products;
