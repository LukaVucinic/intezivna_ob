import Card from "./Card.jsx";
import Button from "./Button.jsx";

export default function ProductCard({
  id,
  title,
  price,
  image,
  isFeatured,
  category,
  rating,
  onAdd,
  onDetails,
}) {
  const renderRating = () => {
    const stars = [];
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 !== 0;

    for (let i = 0; i < fullStars; i++) {
      stars.push("★");
    }

    if (hasHalfStar) {
      stars.push("☆");
    }

    while (stars.length < 5) {
      stars.push("☆");
    }

    return stars.join("");
  };

  return (
    <Card>
      <Card.Header>
        {isFeatured && <span className="badge">Izdvojeno</span>}
        <h3 className="card-title">{title}</h3>
        <div className="card-category">{category}</div>
      </Card.Header>
      <Card.Media>
        <img src={image} alt={title} className="card-image" />
      </Card.Media>
      <Card.Body>
        <div className="card-rating" title={`Ocjena: ${rating}`}>
          {renderRating()}
        </div>
        <div className="card-price">{price.toFixed(2)} €</div>
        <p>
          Ovaj proizvod nudi vrhunske performanse i dugotrajnu izdržljivost.
          Savršen je za svakodnevnu upotrebu.
        </p>
      </Card.Body>
      <Card.Actions>
        <Button variant="details" onClick={() => onDetails(id)}>
          Detalji
        </Button>
        <Button onClick={() => onAdd(id)}>Dodaj u korpu</Button>
      </Card.Actions>
    </Card>
  );
}
