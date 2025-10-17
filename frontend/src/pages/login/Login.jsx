import { useState } from 'react';
import api from '../../api/axios';
import { useNavigate } from 'react-router-dom';
import styles from './Login.module.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    try {
      const res = await api.post('/auth/login', formData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });

      sessionStorage.setItem('access_token', res.data.access_token);

      navigate('/dashboard');
    } catch (err) {
      alert('Login failed');
    }
  };

  return (
    <div className={styles.loginContainer}>
      <h1 className={styles.loginTitle}>LOGIN</h1>
      <form onSubmit={handleLogin} className={styles.loginForm}>
        <input
          className={styles.inputField}
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Username"
          required
        />
        <input
          className={styles.inputField}
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
          required
        />
        <button type="submit" className={styles.loginButton}>Login</button>
      </form>
    </div>
  );
};

export default Login;
