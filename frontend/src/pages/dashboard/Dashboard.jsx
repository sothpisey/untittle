import { useState } from 'react';
import styles from './Dashboard.module.css';
import UserProfile from '../userprofile/UserProfile';
import Products from '../products/Products'

const logout = () => {
        sessionStorage.removeItem('access_token');
        window.location.href = '/login';
      }

const Dashboard = () => {
  const [activeIndex, setActiveIndex] = useState(0);

  return (
    <>
      <div className='header'>
        <div className={styles.topBar}>
          <h2 className={styles.dashboardTitle}>Dashboard</h2>
          <input type="text" name="search" id="search" placeholder="Search..." className={styles.searchInput}/>
          <button className={styles.logoutButton} onClick={logout}>Logout</button>
        </div>
        <div className={styles.tabContainer}>
          <button
            className={activeIndex === 0 ? styles.tabButton + ' ' + styles.active : styles.tabButton}
            onClick={() => setActiveIndex(0)}
          >   Product</button>
          <button
            className={activeIndex === 1 ? styles.tabButton + ' ' + styles.active : styles.tabButton}
            onClick={() => setActiveIndex(1)}
          >   User Profile</button>
          <button
            className={activeIndex === 2 ? styles.tabButton + ' ' + styles.active : styles.tabButton}
            onClick={() => setActiveIndex(2)}
          >   Tab 3</button>
        </div>
      </div>
      <div className={styles.tabContent}>
        {activeIndex === 0 && <Products />}
        {activeIndex === 1 && <UserProfile />}
        {activeIndex === 2 && <div className={styles.tab3}>This is the content of Tab 3.</div>}
      </div>

    </>
  );
};

export default Dashboard;