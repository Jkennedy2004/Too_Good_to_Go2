import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export class Repartidor {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  nombre: string;

  @Column()
  telefono: string;

  @Column()
  email: string;
}
