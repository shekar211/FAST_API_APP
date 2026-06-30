import {getCompanies} from "../services/CompanyService";
import { useEffect, useState } from "react";
import type { company } from "../types/company";


function CompanyCard() {
    const [companies, setCompanies] = useState<company[]>([]);
    async function fetchCompanies() {
        const companies = await getCompanies();
        setCompanies(companies);
    }
    useEffect(() => {
        fetchCompanies();
    }, []);

    return (
        <div className="company-card">
            <h2>Google</h2>
            <p>Welcome to Google</p>
        </div>
    )
}

export default CompanyCard