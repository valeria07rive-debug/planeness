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
import express from "express";
import { getFlights } from "../controllers/flightsController.js";

const router = express.Router();

router.get("/", getFlights);

export default router;