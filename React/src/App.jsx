import { useState, useMemo } from "react";
import "./App.css";
import Header from "./components/Header";
import Footer from "./components/Footer";
import ProductGrid from "./components/ProductGrid";
import Toolbar from "./components/Toolbar";
import CartSidebar from "./components/CartSidebar";
import { PRODUCTS as products } from "./data/products";

function App() {
  const [cart, setCart] = useState([]);
  const [showCart, setShowCart] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [notification, setNotification] = useState({
    show: false,
    message: "",
    error: false,
  });
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("");
  const [featuredOnly, setFeaturedOnly] = useState(false);
  const [sortOption, setSortOption] = useState("default");
  const [discountCode, setDiscountCode] = useState("");

  const categories = useMemo(() => {
    const uniqueCategories = [
      ...new Set(products.map((product) => product.category)),
    ];
    return uniqueCategories;
  }, [products]);

  const filteredAndSortedProducts = useMemo(() => {
    let result = [...products];

    if (searchQuery) {
      const query = searchQuery.toLowerCase();
      result = result.filter(
        (product) =>
          product.title.toLowerCase().includes(query) ||
          product.category.toLowerCase().includes(query)
      );
    }

    if (selectedCategory) {
      result = result.filter(
        (product) => product.category === selectedCategory
      );
    }

    if (featuredOnly) {
      result = result.filter((product) => product.isFeatured);
    }

    switch (sortOption) {
      case "price-asc":
        result.sort((a, b) => a.price - b.price);
        break;
      case "price-desc":
        result.sort((a, b) => b.price - a.price);
        break;
      case "rating-desc":
        result.sort((a, b) => b.rating - a.rating);
        break;
      default:
        break;
    }

    return result;
  }, [products, searchQuery, selectedCategory, featuredOnly, sortOption]);

  const handleAddToCart = (productId) => {
    const product = products.find((p) => p.id === productId);
    setCart((prevCart) => {
      const existingItem = prevCart.find((item) => item.id === productId);

      if (existingItem) {
        return prevCart.map((item) =>
          item.id === productId
            ? { ...item, quantity: item.quantity + 1 }
            : item
        );
      } else {
        return [...prevCart, { ...product, quantity: 1 }];
      }
    });

    showNotification(`Dodato u korpu: ${product.title}`);
  };

  const handleUpdateQuantity = (productId, newQuantity) => {
    if (newQuantity < 1) return;

    setCart((prevCart) =>
      prevCart.map((item) =>
        item.id === productId ? { ...item, quantity: newQuantity } : item
      )
    );
  };

  const handleRemoveItem = (productId) => {
    setCart((prevCart) => prevCart.filter((item) => item.id !== productId));
    showNotification("Proizvod uklonjen iz korpe");
  };

  const handleCheckout = () => {
    setIsProcessing(true);

    // simulacija
    setTimeout(() => {
      setIsProcessing(false);
      setCart([]);
      setShowCart(false);
      setDiscountCode("");
      showNotification("Kupovina je uspjesno obavljena! Hvala vam.", false);
    }, 2000);
  };

  const handleDetails = (productId) => {
    const product = products.find((p) => p.id === productId);
    alert(
      `Detalji proizvoda: ${product.title}\nCijena: ${product.price.toFixed(
        2
      )} €\nKategorija: ${product.category}\nOcjena: ${product.rating}\n${
        product.isFeatured ? "IZDVOJENO!" : ""
      }`
    );
  };

  const showNotification = (message, error = false) => {
    setNotification({ show: true, message, error });
    setTimeout(() => {
      setNotification({ show: false, message: "", error: false });
    }, 3000);
  };

  return (
    <div className="app">
      <head>
        <title>Mini Katalog</title>
        <meta name="description" content="Mini katalog proizvoda" />
      </head>

      <Header cart={cart} onCartClick={() => setShowCart(!showCart)} />

      <div className="container">
        <div className="main-content">
          <Toolbar
            searchQuery={searchQuery}
            onSearchChange={setSearchQuery}
            selectedCategory={selectedCategory}
            onCategoryChange={setSelectedCategory}
            featuredOnly={featuredOnly}
            onFeaturedChange={setFeaturedOnly}
            sortOption={sortOption}
            onSortChange={setSortOption}
            categories={categories}
          />

          <ProductGrid
            products={filteredAndSortedProducts}
            onAdd={handleAddToCart}
            onDetails={handleDetails}
          />
        </div>
        {showCart && (
          <CartSidebar
            cart={cart}
            onUpdateQuantity={handleUpdateQuantity}
            onRemoveItem={handleRemoveItem}
            onCheckout={handleCheckout}
            isProcessing={isProcessing}
            discountCode={discountCode}
            onDiscountChange={setDiscountCode}
            onClose={() => setShowCart(false)}
          />
        )}
      </div>

      <Footer />

      <div
        className={`cart-notification ${
          notification.message ? "message" : ""
        } ${notification.error ? "error" : ""} ${
          notification.message ? "show" : ""
        }`}
      >
        {notification.message}
      </div>
    </div>
  );
}

export default App;
