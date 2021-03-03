import { Entity } from './entity';
const entities: Entity[] =  [
    {entityId: 'urn:ngsi-ld:Device:Autobuses-Volume', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:WeatherObserved:WeatherObserved-2', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:WeatherObserved:WeatherObserved-1', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Alert:ES-Alert-AlicanteBenalua-13-2120201216-02', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Alert:ES-Alert-AlicanteBenalua20201216-02', service: 'alicante'},
    {entityId: 'Consumption:Spain-Consumption-Alicante-Benalua20201216-02', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Benalua-Volume', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Benalua-Flow', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Autobuses-Volume', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Autobuses-Flow', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Diputacion-Volume', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Diputacion-Flow', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Mercado-Volume', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Mercado-Flow', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Alipark-Volume', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Alipark-Flow', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Montaneta-Volume', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Montaneta-Flow', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Rambla-Volume', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Rambla-Flow', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:Device:Device-test', service: 'alicante'},
    {entityId: 'urn:ngsi-ld:WeatherObserved:WeatherObserved', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-0', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-1', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-2', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-3', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-0', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-1', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-2', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-3', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-0', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-1', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-2', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-3', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-5770', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-5771', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-5772', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-5773', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-2182', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-5980', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-5981', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-5982', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-test', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-test2', service: 'braila'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-test', service: 'braila'},
    {entityId: 'PlantsWateringPredicted:CH-PlantsWateringPredicted-Carouge-20201215-19', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-318505H498', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-211306H360', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-211106H360', service: 'braila'},
    {entityId: 'urn:ngsi-ld:Device:Device-211206H360', service: 'braila'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-0', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-1', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-2', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-3', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-0', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-1', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-2', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-3', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-0', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-1', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-2', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-3', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-3', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-4', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-5', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-6', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-7', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-8', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-2', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WaterQualityObserved:Fountain-1', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FountainUsageObserved:Fountain-1', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WaterQualityForecast:Fountain-1', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WeatherObserved:WeatherObserved', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-1', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:Device:Device-0972', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:Device:Device-0a35', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:Device:Device-0a6a', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:Device:Device-0a7c', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:Device:Device-0a7d', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:Device:Device-0a80', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:Device:Device-0a81', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:Device:Device-0a83', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:Device:Device-1f0d', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-test', service: 'carouge'},
    {entityId: 'PlantsWateringPredicted:CH-PlantsWateringPredicted-Carouge-20201215-19', service: 'carouge'},
    {entityId: 'PlantsWateringPredicted:CH-PlantsWateringPredicted-Carouge-test-20201215-19', service: 'carouge'},
    {entityId: 'Alert:1', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-15', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-200', service: 'carouge'},
    {entityId: 'Alert:200', service: 'carouge'},
    {entityId: 'Alert:201', service: 'carouge'},
    {entityId: 'Alert:50', service: 'carouge'},
    {entityId: 'Alert:', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-51', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:FlowerBed:FlowerBed-9', service: 'carouge'},
    {entityId: 'urn:ngsi-ld:WaterQualityObserved:WaterTreatmentPlant', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WaterQualityForecast:WaterTreatmentPlant', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherObserved:WeatherObserved', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-0', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-1', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-2', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day0-3', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-0', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-1', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-2', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day1-3', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-0', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-1', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-2', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WeatherForecast:WeatherForecast-Day2-3', service: 'wtp_lab'},
    {entityId: 'urn:ngsi-ld:WaterQualityObservedFake:WaterQualityObservedFake', service: 'wtp_lab'}
];

export { entities };
