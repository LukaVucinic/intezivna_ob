export default function Card({ children, className = "" }) {
  return <div className={`card ${className}`}>{children}</div>;
}

Card.Header = ({ children }) => <div className="card-header">{children}</div>;
Card.Media = ({ children }) => <div className="card-media">{children}</div>;
Card.Body = ({ children }) => <div className="card-body">{children}</div>;
Card.Actions = ({ children }) => <div className="card-actions">{children}</div>;
