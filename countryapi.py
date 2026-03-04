import express from "express";
const router = express.Router();

router.get("/", (req, res) => {
  res.json({ message: "Lista de vuelos" });
});

export default router;

export const getFlights = (req, res) => {
  res.json([
    {
      id: 1,
      airline: "Lotregolpe Experiences",
      destination: "Las Americas"
    }
  ]);
};