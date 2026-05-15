import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { User, Mail, Lock, Eye, EyeOff, ArrowRight } from 'lucide-react';
import { login, signup } from './api/authApi.js';
import { getUserData } from './api/userApi.js';
import msuLogo from './assets/msuWhite1.png';
import './assets/Auth.css';

const SCORE_LABELS = ['—', 'Weak', 'Fair', 'Good', 'Strong'];
const SCORE_COLORS = ['#1a2b20', '#ef4444', '#f59e0b', '#22c55e', '#22c55e'];

function computePasswordScore(pw) {
  let score = 0;
  if (pw.length >= 8) score++;
  if (pw.length >= 12) score++;
  if (/[a-z]/.test(pw) && /[A-Z]/.test(pw)) score++;
  if (/\d/.test(pw) && /[^a-zA-Z0-9]/.test(pw)) score++;
  return score;
}

function PasswordStrength({ score }) {
  return (
    <div className="pw-strength">
      <div className="pw-segments" role="presentation">
        {[0, 1, 2, 3].map(i => (
          <div
            key={i}
            className="pw-segment"
            style={{ background: i < score ? SCORE_COLORS[score] : 'var(--ink-700)' }}
          />
        ))}
      </div>
      <div className="pw-strength-row">
        <span className="pw-strength-label">Password strength</span>
        <span
          className="pw-strength-level"
          aria-live="polite"
          aria-atomic="true"
          style={{ color: SCORE_COLORS[score] }}
        >
          {SCORE_LABELS[score]}
        </span>
      </div>
    </div>
  );
}

function BrandPane() {
  return (
    <div className="auth-brand" aria-hidden="true">
      <div className="brand-dots" />
      <div className="brand-stripe" />
      <div className="brand-glyph">
        <div className="brand-glyph-ring" />
      </div>

      <div className="brand-top">
        <img src={msuLogo} alt="" className="brand-logo" />
        <span className="brand-wordmark">MSUtrition</span>
      </div>

      <div className="brand-center">
        <p className="brand-eyebrow">
          <span className="pulse-dot" />
          Today's fuel · live
        </p>
        <h2 className="brand-headline">
          Train smart.<br />
          Eat <em>Spartan</em>.
        </h2>
        <p className="brand-subhead">
          Track every macro, micro and meal — purpose-built for Michigan State
          athletes, students, and the dining halls they live in.
        </p>
        <div className="brand-stats">
          <div className="stat-card" style={{ '--stat-color': '#22c55e' }}>
            <span className="stat-label">Calories</span>
            <span className="stat-number">1,584</span>
            <span className="stat-unit">/ 2,200</span>
          </div>
          <div className="stat-card" style={{ '--stat-color': '#3b82f6' }}>
            <span className="stat-label">Protein</span>
            <span className="stat-number">84</span>
            <span className="stat-unit">g</span>
          </div>
          <div className="stat-card" style={{ '--stat-color': '#ef4444' }}>
            <span className="stat-label">Carbs</span>
            <span className="stat-number">202</span>
            <span className="stat-unit">g</span>
          </div>
        </div>
      </div>

      <div className="brand-footer">
        <span>v1.0</span>
        <span className="brand-sep">·</span>
        <span>© MSU 2026</span>
        <span className="brand-sep">·</span>
        <span>Go Green</span>
      </div>
    </div>
  );
}

function Auth({ setIsLoggedIn, setAppUsername }) {
  const navigate = useNavigate();
  const [mode, setMode] = useState('login');
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState(null);
  const [fieldErrors, setFieldErrors] = useState({});

  const isLogin = mode === 'login';
  const passwordScore = computePasswordScore(password);
  const canSubmit = isLogin
    ? username.trim().length > 0 && password.length > 0
    : username.trim().length > 0 && email.trim().length > 0 && password.length > 0 && confirmPassword.length > 0;

  function clearFieldError(field) {
    setFieldErrors(prev => {
      if (!prev[field]) return prev;
      const next = { ...prev };
      delete next[field];
      return next;
    });
  }

  function validate() {
    const errs = {};
    if (!username || username.length < 3 || username.length > 32 || !/^[a-zA-Z0-9_]+$/.test(username)) {
      errs.username = 'Username must be 3–32 chars (letters, numbers, underscore).';
    }
    if (!password) {
      errs.password = 'Password is required.';
    } else if (!isLogin && passwordScore < 2) {
      errs.password = 'Password must be at least 8 characters with mixed case.';
    }
    if (!isLogin) {
      if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        errs.email = 'Enter a valid email address.';
      }
      if (!confirmPassword || confirmPassword !== password) {
        errs.confirmPassword = 'Passwords do not match.';
      }
    }
    setFieldErrors(errs);
    return Object.keys(errs).length === 0;
  }

  async function handleSubmit(e) {
    e.preventDefault();
    if (!validate()) return;
    setSubmitting(true);
    setError(null);
    try {
      if (isLogin) {
        const res = await login(username, password);
        if (res === 'Success') {
          try {
            const user = await getUserData();
            if (user) setAppUsername(user);
          } catch (err) {
            console.error('Username fetch error', err);
          }
          setIsLoggedIn(true);
          navigate('/');
        }
      } else {
        const res = await signup(username, email, password);
        if (res === 'Success') {
          try {
            const user = await getUserData();
            if (user) setAppUsername(user);
          } catch (err) {
            console.error('Username fetch error', err);
          }
          setIsLoggedIn(true);
          navigate('/onboarding');
        }
      }
    } catch (err) {
      if (err.field) {
        setFieldErrors(prev => ({ ...prev, [err.field]: err.message }));
      } else {
        setError(err.message || 'Something went wrong. Please try again.');
      }
    } finally {
      setSubmitting(false);
    }
  }

  function switchMode(newMode) {
    if (newMode === mode) return;
    setMode(newMode);
    setError(null);
    setFieldErrors({});
    setShowPassword(false);
  }

  return (
    <div className="auth-screen">
      <BrandPane />

      <div className="auth-form-pane">
        <div className="auth-card">

          {/* Segmented control */}
          <div
            role="tablist"
            aria-label="Authentication mode"
            className="seg-control"
            data-mode={mode}
          >
            <div className="seg-thumb" aria-hidden="true" />
            <button
              role="tab"
              aria-selected={isLogin}
              className="seg-btn"
              onClick={() => switchMode('login')}
            >
              Login
            </button>
            <button
              role="tab"
              aria-selected={!isLogin}
              className="seg-btn"
              onClick={() => switchMode('signup')}
            >
              Sign Up
            </button>
          </div>

          {/* Header */}
          <div className="auth-header">
            <p className="auth-eyebrow">
              {isLogin ? 'Welcome back' : 'Create account'}
            </p>
            <h1 className="auth-title">
              {isLogin ? 'Sign in to your fuel log.' : 'Start your Spartan plate.'}
            </h1>
            <p className="auth-subtitle">
              {isLogin
                ? "Pick up where you left off — today's meals are waiting."
                : "Takes under a minute. We'll set goals next."}
            </p>
          </div>

          {/* Form-level error */}
          {error && (
            <div className="auth-error-banner" role="alert">
              {error}
            </div>
          )}

          {/*
            key=mode remounts the form on every mode switch so the
            nth-child stagger animations fire fresh each time.
          */}
          <form className="auth-form" key={mode} onSubmit={handleSubmit} noValidate>

            {/* Username */}
            <div className="field-wrap">
              <div className={`field-shell${fieldErrors.username ? ' has-error' : ''}`}>
                <span className="field-icon" aria-hidden="true"><User size={18} /></span>
                <div className="field-inner">
                  <label className="field-label-text" htmlFor="auth-username">Username</label>
                  <input
                    id="auth-username"
                    type="text"
                    autoComplete="username"
                    placeholder="spartan23"
                    value={username}
                    onChange={e => { setUsername(e.target.value); clearFieldError('username'); }}
                  />
                </div>
              </div>
              {fieldErrors.username && (
                <p className="field-err-msg" role="alert">{fieldErrors.username}</p>
              )}
            </div>

            {/* Email — signup only */}
            {!isLogin && (
              <div className="field-wrap">
                <div className={`field-shell${fieldErrors.email ? ' has-error' : ''}`}>
                  <span className="field-icon" aria-hidden="true"><Mail size={18} /></span>
                  <div className="field-inner">
                    <label className="field-label-text" htmlFor="auth-email">Email</label>
                    <input
                      id="auth-email"
                      type="email"
                      autoComplete="email"
                      placeholder="you@msu.edu"
                      value={email}
                      onChange={e => { setEmail(e.target.value); clearFieldError('email'); }}
                    />
                  </div>
                </div>
                {fieldErrors.email && (
                  <p className="field-err-msg" role="alert">{fieldErrors.email}</p>
                )}
              </div>
            )}

            {/* Password */}
            <div className="field-wrap">
              <div className={`field-shell${fieldErrors.password ? ' has-error' : ''}`}>
                <span className="field-icon" aria-hidden="true"><Lock size={18} /></span>
                <div className="field-inner">
                  <label className="field-label-text" htmlFor="auth-password">Password</label>
                  <input
                    id="auth-password"
                    type={showPassword ? 'text' : 'password'}
                    autoComplete={isLogin ? 'current-password' : 'new-password'}
                    placeholder="••••••••"
                    value={password}
                    onChange={e => { setPassword(e.target.value); clearFieldError('password'); }}
                  />
                </div>
                <button
                  type="button"
                  className="pw-toggle"
                  aria-label={showPassword ? 'Hide password' : 'Show password'}
                  aria-pressed={showPassword}
                  onClick={() => setShowPassword(s => !s)}
                >
                  {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                </button>
              </div>
              {fieldErrors.password && (
                <p className="field-err-msg" role="alert">{fieldErrors.password}</p>
              )}
            </div>

            {/* Password strength — signup only */}
            {!isLogin && <PasswordStrength score={passwordScore} />}

            {/* Confirm password — signup only */}
            {!isLogin && (
              <div className="field-wrap">
                <div className={`field-shell${fieldErrors.confirmPassword ? ' has-error' : ''}`}>
                  <span className="field-icon" aria-hidden="true"><Lock size={18} /></span>
                  <div className="field-inner">
                    <label className="field-label-text" htmlFor="auth-confirm">
                      Confirm Password
                    </label>
                    <input
                      id="auth-confirm"
                      type="password"
                      autoComplete="new-password"
                      placeholder="Re-enter password"
                      value={confirmPassword}
                      onChange={e => { setConfirmPassword(e.target.value); clearFieldError('confirmPassword'); }}
                    />
                  </div>
                </div>
                {fieldErrors.confirmPassword && (
                  <p className="field-err-msg" role="alert">{fieldErrors.confirmPassword}</p>
                )}
              </div>
            )}

            {/* Forgot password — login only */}
            {isLogin && (
              <div className="forgot-wrap">
                <button type="button" className="forgot-btn">
                  Forgot password?
                </button>
              </div>
            )}

            {/* Primary CTA */}
            <button type="submit" className="auth-cta" disabled={submitting || !canSubmit}>
              {submitting
                ? <span className="cta-spinner" role="status" aria-label={isLogin ? 'Signing in…' : 'Creating account…'} />
                : <>
                    {isLogin ? 'Sign in' : 'Create account'}
                    <ArrowRight size={18} strokeWidth={2.5} className="cta-arrow" />
                  </>
              }
            </button>

          </form>


        </div>
      </div>
    </div>
  );
}

export default Auth;
