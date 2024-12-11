const express = require('express');

// Create a web API using express and JavaScript with routes for products and customers
const app = express();
const port = 3000;

app.use(express.json());

const products = [
    { id: 1, name: 'Product A', price: 100 },
    { id: 2, name: 'Product B', price: 200 },
];

const customers = [
    { id: 1, name: 'Customer A', email: 'a@example.com' },
    { id: 2, name: 'Customer B', email: 'b@example.com' },
];

// Routes for products
app.get('/products', (req, res) => {
    res.json(products);
});

app.get('/products/:id', (req, res) => {
    const product = products.find(p => p.id === parseInt(req.params.id));
    if (product) {
        res.json(product);
    } else {
        res.status(404).send('Product not found');
    }
});

app.post('/products', (req, res) => {
    const newProduct = {
        id: products.length + 1,
        name: req.body.name,
        price: req.body.price,
    };
    products.push(newProduct);
    res.status(201).json(newProduct);
});

// Routes for customers
app.get('/customers', (req, res) => {
    res.json(customers);
});

app.get('/customers/:id', (req, res) => {
    const customer = customers.find(c => c.id === parseInt(req.params.id));
    if (customer) {
        res.json(customer);
    } else {
        res.status(404).send('Customer not found');
    }
});

app.post('/customers', (req, res) => {
    const newCustomer = {
        id: customers.length + 1,
        name: req.body.name,
        email: req.body.email,
    };
    customers.push(newCustomer);
    res.status(201).json(newCustomer);
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
