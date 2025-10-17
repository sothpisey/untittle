import { useEffect, useState } from "react";
import api from "../../api/axios";
import styles from "./UserProfile.module.css";

const UserProfile = () => {
  const [userData, setUserData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const response = await api.get("/users/me");
        setUserData(response.data);
      } catch (err) {
        console.error(err);
        setError(
          err.response?.data?.message ||
            err.message ||
            "Failed to fetch user info"
        );
      }
    };

    fetchUser();
  }, []);

  if (error) return <div>Error: {error}</div>;
  if (!userData) return <div>Loading user data...</div>;

  return (
    <div className={styles.content}>
      <div className={styles.userProfileContainer}>
        <h2 className={styles.title}>User Profile</h2>
        <table className={styles.userTable}>
          <tbody>
            <tr>
              <th>Field</th>
              <th>Value</th>
            </tr>
            <tr>
              <td>Username</td>
              <td>{userData.username}</td>
            </tr>
            <tr>
              <td>Full Name</td>
              <td>{userData.full_name}</td>
            </tr>
            <tr>
              <td>Email</td>
              <td>{userData.email}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default UserProfile;
