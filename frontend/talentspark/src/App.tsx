import NavBar from "./components/NavBar";
import Welcome from "./components/Welcome";
import Footer from "./components/footer";
import CompanyCard from "./components/CompanyCard";
import JobCard from "./components/JobCard";
import {useState,useEffect} from "react";
import { getCompany } from "./services/CompanyService";
import type { company } from "./types/company";


function App() {
  const[loading,setLoading]=useState(true);
  const[error,setError]=useState<Error|null>(null);
  const[companies,setCompanies]=useState<company[]>([]);
  async function fetchCompanies(){
    setLoading(true);
    try{
      const companies=await getCompany();
      setCompanies(companies);
    } catch (err) {
      setError(err as Error);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchCompanies();
  }, []);

  const handleAddCompany = (companyToAdd: company) => {
    setCompanies((prevCompanies) => [...prevCompanies, companyToAdd]);
  };

  const handleEditCompany = (updatedCompany: company) => {
    setCompanies((prevCompanies) =>
      prevCompanies.map((item) => (item.id === updatedCompany.id ? updatedCompany : item))
    );
  };

  const handleDeleteCompany = (id: number) => {
    setCompanies((prevCompanies) => prevCompanies.filter((item) => item.id !== id));
  };

  if(loading){
    return <div>Loading...</div>;
  }

  if(error){
    return <div>Error: {error.message}</div>;
  }

  return (
    <>
      <NavBar />
      <Welcome />
      <CompanyCard
        companies={companies}
        onadd={handleAddCompany}
        onedit={handleEditCompany}
        ondelete={handleDeleteCompany}
      />
      <JobCard />
      <Footer />
    </>
  );
}
  
export default App;