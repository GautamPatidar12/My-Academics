'''a="Learning Python"

print(a[6])
print(a[9])
print(a[3])
print(a[-5])

print(a[0:9])
print(a[9:])

for i in a:
    print(i ,end=" ")

print("\n")

for i in range(len(a)):
    print(a[i],end=" ")

print("\n")

for i in range(0,len(a),3):
    print(a[i],end=" ")

for i in range(-1,-len(a)-1,-1):
    print(a[i],end=" ")

print(a[-1::-1])
print(a[::])
print(a[::1])
print(a[::2])
print(a[2:9:2])'''


a=eval(input("Give the string"))

b=a[::]
c=a[-1::-1]
if(b==c):
    print("It is palindrom")
else:
    print("It is no palindrom")



















































'''


import React from 'react';

// Sample data for doctors
const doctorData = [
  {
    id: 1,
    name: 'Dr. John Doe',
    image: 'https://via.placeholder.com/150', // Placeholder image
    qualification: 'MBBS, MD',
    experience: '10 years',
  },
  {
    id: 2,
    name: 'Dr. Jane Smith',
    image: 'https://via.placeholder.com/150', // Placeholder image
    qualification: 'MBBS, MS',
    experience: '8 years',
  },
  {
    id: 3,
    name: 'Dr. Emily Johnson',
    image: 'https://via.placeholder.com/150', // Placeholder image
    qualification: 'MBBS, DNB',
    experience: '12 years',
  },
  {
    id: 4,
    name: 'Dr. Robert Brown',
    image: 'https://via.placeholder.com/150', // Placeholder image
    qualification: 'MBBS, MD',
    experience: '15 years',
  },
  {
    id: 5,
    name: 'Dr. Maria Lee',
    image: 'https://via.placeholder.com/150', // Placeholder image
    qualification: 'MBBS, DGO',
    experience: '5 years',
  },
  {
    id: 6,
    name: 'Dr. Mark White',
    image: 'https://via.placeholder.com/150', // Placeholder image
    qualification: 'MBBS, MS',
    experience: '7 years',
  },
  // Add more doctors here
];

function Consultancy({ onBackClick }) {
  return (
    <div className="flex flex-col h-full">
      {/* Back Button */}
      <button
        onClick={onBackClick}
        className="bg-blue-600 text-white p-2 rounded-lg mb-4 self-start"
      >
        Back
      </button>

      {/* Doctor Cards */}
      <div className="overflow-y-auto flex-1">
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {doctorData.map((doctor) => (
            <div
              key={doctor.id}
              className="bg-white p-4 rounded-lg shadow-lg hover:shadow-2xl transition-transform transform hover:scale-105"
            >
              {/* Doctor Image */}
              <img
                src={doctor.image}
                alt={doctor.name}
                className="w-full h-32 object-cover rounded-lg mb-4"
              />
              <h3 className="text-lg font-semibold text-gray-800">{doctor.name}</h3>
              <p className="text-gray-600">{doctor.qualification}</p>
              <p className="text-gray-600">Experience: {doctor.experience}</p>

              {/* Buttons */}
              <div className="mt-4 flex justify-between items-center">
                <button className="bg-green-600 text-white py-1 px-4 rounded-lg hover:bg-green-700 transition-colors duration-300">
                  Call
                </button>
                <button className="bg-blue-600 text-white py-1 px-4 rounded-lg hover:bg-blue-700 transition-colors duration-300">
                  See More
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Consultancy;
















import React, { useState } from 'react';
import DoctorConsultancy from '../../components/Consultancy'; // Import the DoctorConsultancy component

function DashBoard() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [isMobile, setIsMobile] = useState(false);
  const [isDoctorDetailView, setIsDoctorDetailView] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  // Adjust layout for mobile on window resize
  const handleResize = () => {
    if (window.innerWidth <= 1024) {
      setIsMobile(true);
    } else {
      setIsMobile(false);
    }
  };

  React.useEffect(() => {
    window.addEventListener('resize', handleResize);
    handleResize(); // Check on initial load

    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  const handleCardClick = (cardType) => {
    if (cardType === 'doctor') {
      setIsDoctorDetailView(true);
    }
  };

  const handleBackClick = () => {
    setIsDoctorDetailView(false);
  };

  // JSON format for card data
  const cardsData = [
    {
      id: 1,
      title: 'Doctor Consultancy',
      description: 'Click to view doctor details...',
      backgroundColor: 'bg-blue-100',
      textColor: 'text-blue-600',
      onClick: () => handleCardClick('doctor'),
    },
    {
      id: 2,
      title: 'Card 2',
      description: 'Some content here...',
      backgroundColor: 'bg-green-100',
      textColor: 'text-green-600',
      onClick: () => {},
    },
    {
      id: 3,
      title: 'Card 3',
      description: 'Some content here...',
      backgroundColor: 'bg-yellow-100',
      textColor: 'text-yellow-600',
      onClick: () => {},
    },
    {
      id: 4,
      title: 'Card 4',
      description: 'Some content here...',
      backgroundColor: 'bg-red-100',
      textColor: 'text-red-600',
      onClick: () => {},
    },
    {
      id: 5,
      title: 'Card 5',
      description: 'Some content here...',
      backgroundColor: 'bg-blue-100',
      textColor: 'text-blue-600',
      onClick: () => {},
    },
    {
      id: 6,
      title: 'Card 6',
      description: 'Some content here...',
      backgroundColor: 'bg-green-100',
      textColor: 'text-green-600',
      onClick: () => {},
    },
  ];

  return (
    <div className="flex h-screen bg-gray-100 relative">
      {/* Overlay for Sidebar on Mobile */}
      <div
        className={`fixed inset-0 bg-gray-800 bg-opacity-50 lg:hidden transition-opacity ${isSidebarOpen ? 'opacity-100' : 'opacity-0'}`}
        onClick={toggleSidebar}
      ></div>

      {/* Sidebar */}
      <div
        className={`bg-gray-900 text-white w-64 h-full fixed top-0 left-0 transition-all duration-300 transform ${isSidebarOpen ? 'translate-x-0' : '-translate-x-full'} lg:translate-x-0`}
      >
        <div className="flex items-center justify-center py-5 text-2xl font-semibold">
          Dashboard
        </div>
        <ul>
          <li className="py-2 px-6 hover:bg-gray-700 cursor-pointer">Home</li>
          <li className="py-2 px-6 hover:bg-gray-700 cursor-pointer">Settings</li>
          <li className="py-2 px-6 hover:bg-gray-700 cursor-pointer">Profile</li>
          <li className="py-2 px-6 hover:bg-gray-700 cursor-pointer">Messages</li>
        </ul>
      </div>

      {/* Main Content */}
      <div
        className={`flex-1 p-6 transition-all duration-300 ${isSidebarOpen ? 'ml-64' : 'ml-0'} lg:ml-64`}
      >
        {/* Top Bar for Search and Button */}
        <div className={`flex items-center justify-between mb-8 ${isMobile ? 'flex-col' : 'flex-row'}`}>
          {/* Search Bar */}
          <div className="flex items-center w-full max-w-3xl">
            <input
              type="text"
              placeholder="Search..."
              className="w-full px-4 py-2 rounded-lg shadow-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            {/* Submit Button */}
            <button
              className={`ml-4 py-2 px-4 rounded-full bg-blue-600 text-white shadow-md hover:bg-blue-700 transition-all duration-300 ${isMobile ? 'w-10 h-10' : 'px-6'}`}
            >
              {isMobile ? '→' : 'Submit'}
            </button>
          </div>
        </div>

        {/* Conditional Rendering of Content */}
        {isDoctorDetailView ? (
          // Render DoctorConsultancy component
          <DoctorConsultancy onBackClick={handleBackClick} />
        ) : (
          // Render Cards from JSON data
          <div className="bg-white p-6 rounded-lg shadow-xl">
            <h2 className="text-3xl font-semibold text-gray-800 mb-4">Main Dashboard</h2>
            <p className="text-lg text-gray-600">Welcome to your modern and beautiful dashboard. Here you can manage your data and get insights.</p>

            {/* Render Cards using map() */}
            <div className="mt-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {cardsData.map((card) => (
                <div
                  key={card.id}
                  onClick={card.onClick}
                  className={`${card.backgroundColor} p-6 rounded-lg shadow-lg transform transition-all hover:scale-105 hover:shadow-2xl hover:border-2 hover:border-blue-600 cursor-pointer`}
                >
                  <h3 className={`text-xl font-semibold ${card.textColor}`}>{card.title}</h3>
                  <p className="text-gray-600 mt-2">{card.description}</p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Sidebar Toggle Button (for Mobile) */}
      <button
        className="lg:hidden absolute top-16 left-5 bg-blue-600 text-white p-2 rounded-lg"
        onClick={toggleSidebar}
      >
        &#9776;
      </button>
    </div>
  );
}

export default DashBoard;'''