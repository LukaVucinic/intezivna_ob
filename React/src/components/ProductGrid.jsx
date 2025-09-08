import ProductCard from "./ProductCard";

export default function ProductGrid({ products, onAdd, onDetails }) {
  if (products.length === 0) {
    return (
      <div className="no-products">
        <h3>Nema pronadjenih proizvoda</h3>
        <p>Promijeni kriterijume pretrage ili filtere</p>
      </div>
    );
  }

  return (
    <div className="product-grid">
      {products.map((product) => (
        <ProductCard
          key={product.id}
          id={product.id}
          title={product.title}
          price={product.price}
          image={product.image}
          category={product.category}
          rating={product.rating}
          isFeatured={product.isFeatured}
          onAdd={onAdd}
          onDetails={onDetails}
        />
      ))}
    </div>
  );
}
