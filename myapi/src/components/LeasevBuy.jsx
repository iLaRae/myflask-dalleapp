import { useState } from 'react';

function presentValue(rate, cashFlows) {
    return cashFlows.reduce((pv, cashFlow, i) => pv + cashFlow / Math.pow(1 + rate, i + 1), 0);
}

function LeaseVsBuyCalculator() {
    const [leasePayments, setLeasePayments] = useState('');
    const [buyCost, setBuyCost] = useState('');
    const [discountRate, setDiscountRate] = useState('');
    const [residualValue, setResidualValue] = useState('');
    const [result, setResult] = useState('');

    const analyze = () => {
        const paymentsArray = leasePayments.split(',').map(Number);
        const pvLease = presentValue(parseFloat(discountRate), paymentsArray) + parseFloat(residualValue) / Math.pow(1 + parseFloat(discountRate), paymentsArray.length);
        const pvBuy = parseFloat(buyCost);

        setResult(pvLease < pvBuy ? 'Lease' : 'Buy');
    };

    return (
        <div>
            <h2>Lease vs Buy Analysis</h2>
            <label>
                Lease Payments (comma-separated): 
                <input type="text" value={leasePayments} onChange={(e) => setLeasePayments(e.target.value)} />
            </label>
            <br />
            <label>
                Purchase Cost: 
                <input type="text" value={buyCost} onChange={(e) => setBuyCost(e.target.value)} />
            </label>
            <br />
            <label>
                Discount Rate: 
                <input type="text" value={discountRate} onChange={(e) => setDiscountRate(e.target.value)} />
            </label>
            <br />
            <label>
                Residual Value: 
                <input type="text" value={residualValue} onChange={(e) => setResidualValue(e.target.value)} />
            </label>
            <br />
            <button onClick={analyze}>Analyze</button>
            <h3>Result: {result}</h3>
        </div>
    );
}

export default LeaseVsBuyCalculator;
