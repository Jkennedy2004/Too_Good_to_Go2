import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export class RutaEntrega {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  nombreRuta: string;

  @Column()
  descripcion: string;
}
