import { useRef, useEffect } from "react";
import Button from "./Button";

export default function CartSidebar({
  cart,
  onUpdateQuantity,
  onRemoveItem,
  onCheckout,
  isProcessing,
  discountCode,
  onDiscountChange,
  onClose,
}) {
  const closeButtonRef = useRef();

  const subtotal = cart.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );
  const discount = discountCode === "SAVE10" ? subtotal * 0.1 : 0;
  const total = subtotal - discount;

  useEffect(() => {
    if (closeButtonRef.current) {
      closeButtonRef.current.focus();
    }
  }, []);

  return (
    <div className="cart-sidebar">
      <div className="cart-header">
        <h2 className="cart-title">Korpa</h2>
        <Button variant="outline" ref={closeButtonRef} onClick={onClose}>
          X
        </Button>
      </div>

      {cart.length === 0 ? (
        <div className="no-products">
          <p>Vasa korpa je prazna</p>
        </div>
      ) : (
        <>
          <div className="cart-items">
            {cart.map((item) => (
              <div key={item.id} className="cart-item">
                <img
                  src={item.image}
                  alt={item.title}
                  className="cart-item-image"
                />
                <div className="cart-item-details">
                  <div className="cart-item-title">{item.title}</div>
                  <div className="cart-item-price">
                    {item.price.toFixed(2)} €
                  </div>
                  <div className="cart-item-actions">
                    <button
                      className="quantity-btn"
                      onClick={() =>
                        onUpdateQuantity(item.id, item.quantity - 1)
                      }
                      disabled={item.quantity <= 1}
                    >
                      -
                    </button>
                    <input
                      type="number"
                      min="1"
                      className="quantity-input"
                      value={item.quantity}
                      onChange={(e) =>
                        onUpdateQuantity(item.id, parseInt(e.target.value) || 1)
                      }
                    />
                    <button
                      className="quantity-btn"
                      onClick={() =>
                        onUpdateQuantity(item.id, item.quantity + 1)
                      }
                    >
                      +
                    </button>
                    <button
                      className="remove-item"
                      onClick={() => onRemoveItem(item.id)}
                    >
                      Ukloni
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="cart-summary">
            <div className="summary-row">
              <span className="summary-label">Ukupna vrijednost:</span>
              <span className="summary-value">{subtotal.toFixed(2)} €</span>
            </div>

            <div className="summary-row">
              <div>
                <span className="summary-label">Popust:</span>
                <span className="discount-value">-{discount.toFixed(2)} €</span>
                <input
                  type="text"
                  placeholder="Unesite kupon"
                  className="discount-input"
                  value={discountCode}
                  onChange={(e) => onDiscountChange(e.target.value)}
                />
              </div>
            </div>

            <div className="summary-row cart-total">
              <span className="summary-label">Ukupno:</span>
              <span className="summary-value">{total.toFixed(2)} €</span>
            </div>

            <button
              className="checkout-btn"
              onClick={onCheckout}
              disabled={cart.length === 0 || isProcessing}
            >
              {isProcessing ? "Obrada..." : "Zavrsi kupovinu"}
            </button>
          </div>
        </>
      )}
    </div>
  );
}
