function Header({ cart, onCartClick }) {
  const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
  const totalPrice = cart.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );

  return (
    <header>
      <div className="header-title">Mini Katalog</div>
      <div className="cart-summary-header" onClick={onCartClick}>
        <div className="cart-icon">
          🛒
          {totalItems > 0 && <span className="cart-count">{totalItems}</span>}
        </div>
        <div>{totalPrice.toFixed(2)} €</div>
      </div>
    </header>
  );
}

export default Header;
