// Parte 1 - comandos ejecutados en mongosh (base de datos  HuilaSoft)

use("HuilaSoft")

// ---------- Agentes ----------
db.Agentes.insertMany([
  { nombre: "Laura Cerquera", nivel: "senior", ticketsh: 10, turno: "lunes" },
  { nombre: "Andrés Perdomo", nivel: "junior", ticketsh: 6, turno: "no" }
])

// ---------- Ticket (cada ticket guarda el id del agente que lo atendió) ----------
let laura = db.Agentes.findOne({ nombre: "Laura Cerquera" })

db.Ticket.insertMany([
  { codigo: "T1", minllegada: 0,  atencion: 5, prioridad: "alta",  agente_id: laura._id },
  { codigo: "T2", minllegada: 3,  atencion: 7, prioridad: "alta",  agente_id: laura._id },
  { codigo: "T3", minllegada: 6,  atencion: 4, prioridad: "media", agente_id: laura._id },
  { codigo: "T4", minllegada: 14, atencion: 8, prioridad: "baja",  agente_id: laura._id },
  { codigo: "T5", minllegada: 25, atencion: 6, prioridad: "alta",  agente_id: laura._id },
  { codigo: "T6", minllegada: 28, atencion: 5, prioridad: "media", agente_id: laura._id },
  { codigo: "T7", minllegada: 40, atencion: 9, prioridad: "baja",  agente_id: laura._id },
  { codigo: "T8", minllegada: 52, atencion: 4, prioridad: "alta",  agente_id: laura._id }
])

// ---------- Pruebas ----------
db.Pruebas.insertMany([
  { semana: 1, ndefectos: 28 },
  { semana: 2, ndefectos: 23 },
  { semana: 3, ndefectos: 22 },
  { semana: 4, ndefectos: 17 },
  { semana: 5, ndefectos: 16 },
  { semana: 6, ndefectos: 12 },
  { semana: 7, ndefectos: 12 },
  { semana: 8, ndefectos: 9 }
])

// ---------- Consultas ----------
// tickets de prioridad alta
db.Ticket.find({ prioridad: "alta" })

// tickets con atención mayor a 6 minutos
db.Ticket.find({ atencion: { $gt: 6 } })

// semanas con menos de 15 defectos
db.Pruebas.find({ ndefectos: { $lt: 15 } })

// ---------- Actualización ----------
// el ticket T7 pasa a prioridad media
db.Ticket.updateOne({ codigo: "T7" }, { $set: { prioridad: "media" } })

// ---------- Eliminación ----------
// se crea un documento de prueba y se borra
db.Ticket.insertOne({ codigo: "PRUEBA", minllegada: 99, atencion: 1, prioridad: "baja" })
db.Ticket.deleteOne({ codigo: "PRUEBA" })


