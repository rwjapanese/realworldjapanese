export const CLUSTERS = [
  { id: "keigo", label: "Keigo" },
  { id: "business-email", label: "Business Email" },
  { id: "meetings", label: "Meetings & Phone" },
  { id: "workplace-culture", label: "Workplace Culture" },
  { id: "tech-japanese", label: "Tech Japanese" },
  { id: "daily-office", label: "Daily Office" },
] as const;

export type ClusterId = (typeof CLUSTERS)[number]["id"];

export const CLUSTER_IDS = CLUSTERS.map(c => c.id);

export function isValidCluster(id: string): id is ClusterId {
  return CLUSTERS.some(c => c.id === id);
}

export function getClusterLabel(id: string): string {
  return CLUSTERS.find(c => c.id === id)?.label ?? id;
}
