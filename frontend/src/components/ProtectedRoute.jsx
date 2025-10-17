import { Navigate } from "react-router-dom";
import api from "../api/axios";
import { useEffect, useState } from "react";

const ProtectedRoute = ({ children }) => {
  const token = sessionStorage.getItem("access_token");
  const [authorized, setAuthorized] = useState(token ? null : false);

  useEffect(() => {
    if (!token) return;

    let intervalId;

    const verifyToken = async () => {
      try {
        await api.get("/auth/verify", {
          headers: { Authorization: `Bearer ${token}` },
        });
        setAuthorized(true);
      } catch {
        sessionStorage.removeItem("access_token");
        setAuthorized(false);
      }
    };

    verifyToken();

    intervalId = setInterval(verifyToken, 60000);

    return () => clearInterval(intervalId);
  }, [token]);

  if (!token) return <Navigate to="/login" replace />;
  if (authorized === null) return <p>Checking access...</p>;
  return authorized ? children : <Navigate to="/login" replace />;
};

export default ProtectedRoute;