import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export class OfertaReducida {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  descripcion: string;

  @Column({ type: 'decimal' })
  precioReducido: number;

  @Column({ type: 'timestamp' })
  fechaInicio: Date;

  @Column({ type: 'timestamp' })
  fechaFin: Date;
}
