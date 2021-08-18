/*
Core logic/payment from:
https: //stripe.com/docs/payments/accept-a-payment

CSS from:
https: //stripe.com/docs/stripe-js
*/

let stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
let client_secret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripe_public_key);
let elements = stripe.elements();
let style = {
    base: {
        iconColor: '#000',
        color: '#6c6c6f',
        fontWeight: '500',
        fontFamily: 'Noto, serif',
        fontSize: '16px',
        fontSmoothing: 'antialiased',
        ':-webkit-autofill': {
            color: '#fce883',
        },
        '::placeholder': {
            color: '#87BBFD',
        },
    },
    invalid: {
        iconColor: '#dc3545',
        color: '#dc3545',
    },
};
let card = elements.create('card', {
    style: style
});
card.mount('#card-element');