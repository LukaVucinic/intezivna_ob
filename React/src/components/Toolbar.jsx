export default function Toolbar({
  searchQuery,
  onSearchChange,
  selectedCategory,
  onCategoryChange,
  featuredOnly,
  onFeaturedChange,
  sortOption,
  onSortChange,
  categories,
}) {
  return (
    <div className="toolbar">
      <div className="toolbar-group">
        <input
          type="text"
          placeholder="Pretrazi proizvode..."
          className="search-input"
          value={searchQuery}
          onChange={(e) => onSearchChange(e.target.value)}
        />
      </div>

      <div className="toolbar-group">
        <select
          className="select-input"
          value={selectedCategory}
          onChange={(e) => onCategoryChange(e.target.value)}
        >
          <option value="">Sve kategorije</option>
          {categories.map((category) => (
            <option key={category} value={category}>
              {category}
            </option>
          ))}
        </select>
      </div>

      <div className="toolbar-group">
        <label className="checkbox-group">
          <input
            type="checkbox"
            checked={featuredOnly}
            onChange={(e) => onFeaturedChange(e.target.checked)}
          />
          Samo izdvojeni
        </label>
      </div>

      <div className="toolbar-group">
        <select
          className="select-input"
          value={sortOption}
          onChange={(e) => onSortChange(e.target.value)}
        >
          <option value="default">Default</option>
          <option value="price-asc">Cijena: rastuca</option>
          <option value="price-desc">Cijena: opadajuca </option>
          <option value="rating-desc">Ocjena: opdajuca</option>
        </select>
      </div>
    </div>
  );
}
