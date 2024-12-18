import query

if __name__ == "__main__":
    print("1. Продукты в полуинтервале [3, 7):", query.request())
    print(
        "2. Самая дешевая цена в 1 категории:",
        query.get_min_price_by_category(category_id=1),
    )
    print(
        "3. Максимальная цена продукта у каждого поставщика:",
        query.get_max_price_by_suppliers(),
    )