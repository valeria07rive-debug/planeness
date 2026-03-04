import express from "express";

const router = express.Router();

// Controller
const getFlights = (req, res) => {
  res.json([
    {
      id: 1,
      airline: "Lotregolpe Experiences",
      destination: "Las Americas"
    }
  ]);
};

// Route
router.get("/", getFlights);

export default router;