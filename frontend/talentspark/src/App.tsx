import Welcome from "./components/Welcome";
import NavBar from "./components/NavBar";
import CompanyCard from "./components/CompanyCard";
import Footer from "./components/footer";
import {useEffect, useState} from "react";
import {getCompanies} from "./services/CompanyService";
import type { company } from "./types/company";

function App() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);
  const [companies, setCompanies] = useState<company[]>([]);

  async function fetchCompanies() {
    setLoading(true);
    try {
      const companies = await getCompanies();
      setCompanies(companies);
    }
    catch (error) {
      setError(error as Error);
    }
    finally {
      setLoading(false);
    }
  }
  
  useEffect(() => {
    const fetchCompanies = async () => {
      const companies = await getCompanies();
      setCompanies(companies);
    };
    fetchCompanies();
  }, []);

  return (
    <>
    <NavBar />
    <Welcome />
    <CompanyCard />
    <Footer />
    </>
  );
}

export default App; 